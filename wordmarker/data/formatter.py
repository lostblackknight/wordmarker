import logging
import os
from abc import ABCMeta, abstractmethod
from win32com.client import DispatchEx
from win32com.client.gencache import EnsureDispatch
from wordmarker.contexts import SystemContext
from wordmarker.utils import log


class Formatter(metaclass=ABCMeta):
    """
    格式化的抽象类
    """

    @abstractmethod
    def _format(self, *args):
        pass


class DocxFormatter(Formatter, SystemContext):
    """
    将doc文件转换为docx文件
    """

    @log
    def _format(self, doc_path_list: list, docx_path: str):
        EnsureDispatch('Word.Application')
        msword = DispatchEx("Word.Application")
        msword.Visible = False  # 是否可见
        msword.DisplayAlerts = 0
        for doc_path in doc_path_list:
            if doc_path.endswith(".doc") and not doc_path.startswith('~$'):
                # 打开doc文件
                doc = None
                rename = None
                try:
                    doc = msword.Documents.Open(FileName=doc_path)
                    # 重命名
                    rename = os.path.split(doc_path)[1]
                    rename = os.path.splitext(rename)
                    final_file_name = docx_path + self.path_separator + rename[0] + '.docx'
                    # 另存为docx文件
                    doc.SaveAs(FileName=final_file_name, FileFormat=12)
                finally:
                    if doc:
                        doc.Close()
                        self._logger: logging.Logger
                        self._logger.info(
                            "{src}文件，成功转换为 {tgt}文件".format(src=os.path.split(doc_path)[1], tgt=rename[0] + '.docx'))
        msword.Quit()


class SqlFormatter(Formatter):
    """
    格式化sql语句
    """

    def _format(self, sql):
        """
        格式化用户输入的sql

        例如：
            *输入*：     select * from t_user where username=? and password=?

            *格式化*：   select * from t_user where username=:a and password=:b

            *注意*：     拼接的 :a, :b 使用的是26个字母，也就是说一次查询的?，不能超过26个，超过26个后情况未知...
        :param sql: sql语句
        :return: 格式化后的sql语句
        """
        sql_list = list(sql)
        index = 0
        n = 97
        for i in sql_list:
            if i == '?':
                sql_list[index] = ':' + chr(n)
                n += 1
            index += 1
        return ''.join(sql_list)

import logging
import os
from abc import ABCMeta, abstractmethod
from win32com.client import DispatchEx
from win32com.client.gencache import EnsureDispatch
from wordmarker.contexts import SystemContext
from wordmarker.utils import log


class Formatter(metaclass=ABCMeta):
    """
    ::

        格式化的抽象类
    """

    @abstractmethod
    def format(self, *args):
        """
        .. note::

            格式化数据

        :param args: 数据
        :return: - 格式化后的数据
        """
        pass


class SqlFormatter(Formatter):
    """
    ::

        格式化sql语句
    """

    def format(self, sql):
        """
        .. note::

            格式化用户输入的sql语句

            例如：

                .. code-block:: sql
                    :linenos:

                    -- 输入 --
                    select * from t_user where username=? and password=?
                    -- 输出 --
                    select * from t_user where username=:a and password=:b

        .. caution::

            拼接的 ``:a`` ``:b`` 使用的是26个字母，也就是说一次查询的 ``?`` ，不能超过26个。

        :param sql: sql语句
        :return: - 格式化后的sql语句
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

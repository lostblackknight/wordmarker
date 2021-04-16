import os
from typing import Union
from wordmarker.contexts import SystemContext


class PathUtils(SystemContext):
    """
    路径工具类
    """

    def __init__(self, src, tgt):
        self.__src = src
        self.__tgt = tgt

    def get_relative_path(self):
        """
        将两个路径拼接起来

        例子：
            src = c:/a/b/c

            tgt = ../../d/c.txt

            final = c:/a/d/c.txt

            src = c:/a/b/c/foo.txt

            tgt = ../../d/c.txt

            final = c:/a/d/c.txt
        :return: 最终路径
        """
        src: str = self.__src
        tgt: str = self.__tgt
        src = os.path.normpath(src)
        tgt = os.path.normpath(tgt)
        if os.path.isfile(src):
            src_dir = os.path.dirname(src)
        else:
            src_dir = src
        src_list = src_dir.split(self.path_separator)
        tgt_list = tgt.split(self.path_separator)
        index = 0
        for i in tgt_list:
            if i == r'..':
                src_list.pop()
                index += 1
        for i in range(0, index):
            tgt_list.pop(0)
        final_list = src_list + tgt_list
        final_path = self.path_separator.join(final_list)
        return final_path

    @staticmethod
    def filter_file(file_list: Union[list, str], suffix_list: Union[list, str]):
        """
        过滤目录或者文件，通过后缀名

        :param file_list: 文件或目录列表
        :param suffix_list: 后缀或后缀列表
        :return: 过滤后的文件列表
        """
        final_list = []
        if type(file_list) is not list:
            file_list = [file_list]
        for item in file_list:
            file_suffix = os.path.splitext(item)[1]
            if type(suffix_list) is not list:
                suffix_list = [suffix_list]
            if file_suffix in suffix_list:
                final_list.append(item)
        return final_list

import os
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

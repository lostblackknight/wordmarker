import os
from wordmarker.contexts import Context


class SystemContext(Context):
    """
    ::

        系统上下文，获取和系统有关的属性
    """

    def _init(self):
        """
        ::

            初始化系统上下文
        """
        pass

    path_separator = os.sep  # 路径分隔符
    file_separator = os.pathsep  # 文件分隔符

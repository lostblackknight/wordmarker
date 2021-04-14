import os
from wordmarker.contexts import Context


class SystemContext(Context):
    """
    系统上下文，获取和系统有关的属性
    """

    def _init(self):
        pass

    path_separator = os.sep
    file_separator = os.pathsep

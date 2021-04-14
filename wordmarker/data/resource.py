import os
from chardet import UniversalDetector
from wordmarker.contexts import SystemContext
from wordmarker.utils import log


class Resource(SystemContext):
    """
    资源类，包含与资源相关的属性和判断的方法
    """

    @log
    def __init__(self, path, loader):
        self.__path = path
        self.__loader = loader

    def is_file(self):
        """
        判断是否为文件

        :return: 是文件，返回True<br>
                 不是文件，返回False
        """
        return os.path.isfile(self.__path)

    def exists(self):
        """
        判断文件或目录是否存在

        :return: 存在，返回True<br>
                 不存在，返回False
        """
        return os.path.exists(self.__path)

    def get_file_name(self):
        """
        获取文件名

        :return: 是文件，返回文件的名字<br>
                 是目录，返回当前目录下的所有文件的文件名
        """
        if self.exists():
            if self.is_file():
                path, file_name = os.path.split(self.__path)
                return file_name
            else:
                return os.listdir(self.__path)
        else:
            self._logger.error("文件或目录不存在")

    def get_file(self):
        """
        获取文件，返回文件的绝对路径

        :return: 是文件，返回文件的绝对路径<br>
                 是目录，返回当前目录下所有文件的绝对路径
        """
        if self.exists():
            if self.is_file():
                return os.path.abspath(self.__path)
            else:
                file_list = []
                for i in os.listdir(self.__path):
                    file_list.append(os.path.abspath(self.__path + self.path_separator + i))
                return file_list
        else:
            self._logger.error("文件或目录不存在")

    def get_dir(self):
        """
        获取目录，返回目录的绝对路径

        :return: 是目录，返回目录的绝对路径<br>
                 是文件，返回文件所在的目录
        """
        if self.exists():
            if not self.is_file():
                return os.path.abspath(self.__path)
            else:
                path, file_name = os.path.split(self.__path)
                return path
        else:
            self._logger.error("文件或目录不存在")

    def get_file_encoding(self):
        """
        获取文件的编码

        :return: 是文件，获取文件的编码，返回一个文件编码的字符串<br>
                 是目录，获取当前目录下所有文件的编码，返回一个字典<br>
                 key为文件的绝对路径，value为文件的编码
        """
        if self.exists():
            if self.is_file():
                try:
                    with open(self.get_file(), 'rb') as f:
                        detector = UniversalDetector()
                        for line in f.readlines():
                            detector.feed(line)
                            if detector.done:
                                break
                        detector.close()
                        result: dict = detector.result
                        return result.get('encoding')
                except (IOError, ValueError, TypeError) as exc:
                    self._logger.exception("获取文件的编码失败", exc_info=exc)
            else:
                file_list = self.get_file()
                file_encoding = {}
                try:
                    detector = UniversalDetector()
                    for file in file_list:
                        detector.reset()
                        with open(file, 'rb') as f:
                            for line in f.readlines():
                                detector.feed(line)
                                if detector.done:
                                    break
                        detector.close()
                        result: dict = detector.result
                        file_encoding[file] = result.get('encoding')
                    return file_encoding
                except (IOError, ValueError, TypeError) as exc:
                    self._logger.exception("获取文件的编码失败", exc_info=exc)
        else:
            self._logger.error("文件或目录不存在")

    def get_file_name_prefix_suffix(self):
        """
        返回文件的前缀和后缀

        :return: 是文件，获取文件的前缀和后缀，返回一个元组<br>
                 是目录，获取目录下所有文件的前缀和后缀，返回一个字典<br>
                 key为文件名，value为由文件的前缀和后缀组成的元组
        """
        if self.exists():
            if self.is_file():
                file_name = self.get_file_name()
                return os.path.splitext(file_name)
            else:
                p_s_dict = {}
                file_name_list = self.get_file_name()
                for file_name in file_name_list:
                    p_s_dict[file_name] = os.path.splitext(file_name)
                return p_s_dict
        else:
            self._logger.error("文件或目录不存在")

    def get_loader(self):
        """
        获取加载当前资源的加载器

        :return: 加载器
        """
        return self.__loader

import yaml
from wordmarker.data import Resource
from wordmarker.loaders import DefaultResourceLoader
from wordmarker.utils import log


class YamlResourceLoader(DefaultResourceLoader):
    """
    ::

        yaml文件的资源加载器
    """

    @log
    def __init__(self):
        super().__init__()

    def load(self, resource: Resource):
        """
        .. note::

            加载yaml资源

        :param resource: yaml资源实例
        :return: - yaml资源为文件，获取文件中的数据

                 - yaml文件资源为目录，获取目录下所有yaml文件中的数据，返回一个字典

                    - key为文件的绝对路径

                    - value为文件的数据
        """
        if resource.exists():
            if resource.is_file():
                try:
                    with open(resource.get_file(), encoding=resource.get_file_encoding()) as f:
                        data = yaml.safe_load(f.read())
                        return data
                except (IOError, ValueError, TypeError) as exc:
                    self._logger.exception("加载文件时发生错误", exc_info=exc)
            else:
                file_list = resource.get_file()
                encoding_dict = resource.get_file_encoding()
                data_dict = {}
                try:
                    for file in file_list:
                        with open(file, encoding=encoding_dict.get(file)) as f:
                            data = yaml.safe_load(f.read())
                            data_dict[file] = data
                    return data_dict
                except (IOError, ValueError, TypeError) as exc:
                    self._logger.exception("加载文件时发生错误", exc_info=exc)
        else:
            self._logger.error("文件或目录不存在")

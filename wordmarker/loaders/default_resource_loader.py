from wordmarker.data import Resource
from wordmarker.loaders.resource_loader import ResourceLoader
from wordmarker.utils import log


class DefaultResourceLoader(ResourceLoader):
    """
    默认的加载资源的类
    """

    @log
    def __init__(self):
        pass

    def get_resource(self, path=None) -> Resource:
        """
        获取资源

        :param path: 文件或目录
        :return: 资源实例
        """
        return Resource(path, self)

    def load(self, resource: Resource):
        """
        加载资源

        :param resource: 资源实例
        :return: 资源中的数据<br>
                 资源为文件，获取文件中的数据<br>
                 资源为目录，获取目录下所有文件的数据，返回一个字典<br>
                 key为文件的绝对路径，value为文件的数据
        """
        if resource.exists():
            if resource.is_file():
                try:
                    with open(resource.get_file(), encoding=resource.get_file_encoding()) as f:
                        data = f.read()
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
                            data = f.read()
                            data_dict[file] = data
                    return data_dict
                except (IOError, ValueError, TypeError) as exc:
                    self._logger.exception("加载文件时发生错误", exc_info=exc)
        else:
            self._logger.error("文件或目录不存在")

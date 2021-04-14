import yaml
from wordmarker.data import Resource
from wordmarker.loaders import DefaultResourceLoader
from wordmarker.utils import log


class YamlResourceLoader(DefaultResourceLoader):
    """
    加载yaml文件资源的类
    """

    @log
    def __init__(self):
        super().__init__()

    def load(self, resource: Resource):
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

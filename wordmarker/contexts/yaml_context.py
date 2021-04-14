import copy
import os.path

from wordmarker.contexts.context import Context
from wordmarker.loaders.yaml_resource_loader import YamlResourceLoader
from wordmarker.utils import YamlUtils


class YamlContext(Context, YamlResourceLoader):
    """
    yaml文件的上下文
    """

    __yaml_context = None

    def __init__(self, path):
        super().__init__()
        self.__path = path
        self.__data = None
        self._init()

    def _init(self):
        resource = self.get_resource(self.path)
        print(resource.get_file())
        self.__data = self.load(resource)

    def get_yaml(self):
        """
        返回有读取的yaml文件构成的字典

        :return: path为文件，返回一个字典，内容为yaml文件的内容<br>
                 path为目录，返回一个字典，key为yaml文件的绝对路径<br>
                 value为yaml文件的内容，是一个字典
        """
        return self.__data

    def get_value(self, prop):
        """
        从 yaml字典中，根据属性获取对应的值

        加载多个文件，排在后面的文件的文件的值覆盖前面文件的值

        :param prop: 属性，用`.`分隔，例如，mysql.host
        :return: yaml字典中对应的值
        """
        prop_list = prop.split('.')
        if self.get_resource(self.path).is_file():
            yaml_dict = self.get_yaml()
            value = YamlUtils().get_value(yaml_dict, prop_list, prop, self.get_resource(self.path).get_file())
            return value
        else:
            yaml = self.get_yaml()
            value = None
            for key, val in yaml.items():
                temp_list = copy.deepcopy(prop_list)
                v = YamlUtils().get_value(val, temp_list, prop, key)
                if v is not None:
                    value = v
            return value

    @property
    def path(self):
        return self.__path

    @path.setter
    def path(self, path):
        self.__path = path

    def __new__(cls, *args, **kwargs):
        if cls.__yaml_context is None:
            cls.__yaml_context = object.__new__(cls)
        return cls.__yaml_context

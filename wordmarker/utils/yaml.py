import logging
from wordmarker.utils import log


class YamlUtils:
    """
    ::

        yaml文件工具类
    """

    @log
    def __init__(self):
        pass

    def get_value(self, yaml_dict, prop_list, temp_prop, file_name):
        """
        .. note::

            递归调用获取yaml文件中属性对应的值

        :param yaml_dict: yaml文件中的数据，以字典形式存放
        :param prop_list: 属性列表，例如： ``pdbc.engine.url`` -> ``[pdbc, engine, url]``
        :param temp_prop: 临时属性，在日志中进行提示，例如： ``pdbc.engine.url``
        :param file_name: yaml文件名
        :return: - yaml文件中属性对应的值
        """
        prop_list = prop_list
        if (len(prop_list) == 1) and (len(prop_list[0]) == 0):
            self._logger.error("输入的属性的值为空，在{file_name}中获取不到".format(file_name=file_name))
        else:
            value = yaml_dict.get(prop_list.pop(0))
            if type(value) == dict:
                return self.get_value(value, prop_list, temp_prop, file_name)
            else:
                if value is not None:
                    self._logger: logging.Logger
                    self._logger.info(
                        "{file_name}文件中，属性 {prop} 对应的值获取成功".format(file_name=file_name, prop=temp_prop))
                    return value
                else:
                    self._logger: logging.Logger
                    self._logger.warning(
                        "{file_name}文件中，属性 {prop} 对应的值为空。".format(file_name=file_name, prop=temp_prop))

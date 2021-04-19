from abc import ABCMeta, abstractmethod


class ResourceLoader(metaclass=ABCMeta):
    """
    ::

        资源加载器的抽象类
    """

    @abstractmethod
    def get_resource(self, path):
        """
        .. note::

            获取资源

        :param path: 路径
        :return: - 资源
        """
        pass

    @abstractmethod
    def load(self, resource):
        """
        .. note::

            加载资源

        :param resource: 资源
        :return: - 资源中的数据
        """
        pass

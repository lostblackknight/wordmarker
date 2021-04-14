from abc import ABCMeta, abstractmethod


class ResourceLoader(metaclass=ABCMeta):
    """
    资源加载的抽象类
    """

    @abstractmethod
    def get_resource(self, path):
        pass

    @abstractmethod
    def load(self, resource):
        pass

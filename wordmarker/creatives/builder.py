from abc import ABCMeta, abstractmethod


class AbstractBuilder(metaclass=ABCMeta):
    """
    *生成器模式*

    用于构造复杂的对象
    """

    @abstractmethod
    def append(self, *args, **kwargs):
        pass

    @abstractmethod
    def build(self):
        pass

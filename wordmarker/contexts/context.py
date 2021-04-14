from abc import ABCMeta, abstractmethod


class Context(metaclass=ABCMeta):
    """
    所有上下文的公共父类
    """

    @abstractmethod
    def _init(self):
        """
        初始化上下文
        """
        pass

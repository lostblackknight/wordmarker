from abc import ABCMeta, abstractmethod


class AbstractBuilder(metaclass=ABCMeta):
    """
    ::

        用于构造复杂的对象
    """

    @abstractmethod
    def append(self, *args, **kwargs):
        """
        .. note::

            添加对象的部件

        :return: - 当前builder对象
        """
        pass

    @abstractmethod
    def build(self):
        """
        .. note::

            构建复杂对象的实例

        :return: - 复杂对象的实例
        """
        pass

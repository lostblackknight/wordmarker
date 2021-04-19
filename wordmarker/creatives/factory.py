from abc import ABCMeta, abstractmethod
from collections import KeysView


class AbstractBeanFactory(metaclass=ABCMeta):
    """
    ::

        BeanFactory的抽象类
    """

    @abstractmethod
    def get_bean_names(self):
        """
        .. note::

            获取工厂中所有bean实例对应的名字

        :return: - 所有的bean实例对应的名字
        """
        pass

    @abstractmethod
    def get_bean(self, name: str):
        """
        .. note::

            根据bean的名字获取bean实例

        :param name: 名字
        :return: - bean实例
        """
        pass

    @abstractmethod
    def contain_bean(self, name: str):
        """
        .. note::

            判断工厂中是否包含某个bean实例

        :param name: 名字
        :return: - 包含，返回True
                 - 不包含，返回False
        """
        pass

    @abstractmethod
    def get_type(self, name: str):
        """
        .. note::

            获取bean实例的类型

        :param name: 名字
        :return: - 工厂中存在bean实例，返回bean实例的类型
                 - 不存在，返回 None 对应的类型 NoneType
        """
        pass


class BeanFactory(AbstractBeanFactory):
    """
    ::

        AbstractBeanFactory的实现类
    """
    __factory_bean = None
    _beans = {}

    def get_bean_names(self) -> KeysView:
        """
        .. note::

            获取工厂中所有bean实例对应的名字

        :return: - 所有的bean实例对应的名字
        """
        return self._beans.keys()

    def get_bean(self, name: str):
        """
        .. note::

            根据bean的名字获取bean实例

        :param name: 名字
        :return: - bean实例
        """
        return self._beans.get(name)

    def contain_bean(self, name: str):
        """
        .. note::

            判断工厂中是否包含某个bean实例

        :param name: 名字
        :return: - 包含，返回True
                 - 不包含，返回False
        """
        return name in self._beans.keys()

    def get_type(self, name: str):
        """
        .. note::

            获取bean实例的类型

        :param name: 名字
        :return: - 工厂中存在bean实例，返回bean实例的类型
                 - 不存在，返回 None 对应的类型 NoneType
        """
        if self.contain_bean(name):
            return type(self._beans.get(name))
        else:
            return type(None)

    def __new__(cls, *args, **kwargs):
        if cls.__factory_bean is None:
            cls.__factory_bean = object.__new__(cls)
        return cls.__factory_bean


class FactoryBean(BeanFactory):
    """
    ::

        BeanFactory的子类

        通过add_bean方法，将bean实例添加到工厂
    """
    __factory_bean = None

    def __init__(self):
        if not self.contain_bean("factory_bean"):
            # 将自身 factory_bean 添加到工厂
            self.add_bean("factory_bean", self)

    def __new__(cls, *args, **kwargs):
        if cls.__factory_bean is None:
            cls.__factory_bean = object.__new__(cls)
        return cls.__factory_bean

    def add_bean(self, name: str, bean):
        """
        .. note::

            将bean实例添加到工厂

        :param name: 名字
        :param bean: bean实例
        """
        self._beans[name] = bean

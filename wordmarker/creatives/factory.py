from abc import ABCMeta, abstractmethod
from collections import KeysView


class AbstractBeanFactory(metaclass=ABCMeta):
    """
    *工厂模式*

    BeanFactory的抽象类
    """

    @abstractmethod
    def get_bean_names(self):
        pass

    @abstractmethod
    def get_bean(self, name: str):
        pass

    @abstractmethod
    def contain_bean(self, name: str):
        pass

    @abstractmethod
    def get_type(self, name: str):
        pass


class BeanFactory(AbstractBeanFactory):
    """
    AbstractBeanFactory的基本实现类
    """
    __factory_bean = None
    _beans = {}

    def get_bean_names(self) -> KeysView:
        """
        获取工厂中所有bean实例对应的名字

        :return: 所有的bean实例对应的名字
        """
        return self._beans.keys()

    def get_bean(self, name: str):
        """
        根据bean的名字获取bean实例

        :param name: 名字
        :return: bean实例
        """
        return self._beans.get(name)

    def contain_bean(self, name: str):
        """
        判断工厂中是否包含某个bean实例

        :param name: 名字
        :return: 包含返回 True，不包含返回 False
        """
        return name in self._beans.keys()

    def get_type(self, name: str):
        """
        获取bean实例的类型

        :param name: 名字
        :return: 工厂中存在bean实例，返回实例的类型；不存在返回None对应的类型NoneType
        """
        if self.contain_bean(name):
            return type(self._beans.get(name))
        else:
            return type(None)

    def __new__(cls, *args, **kwargs):
        """
        *单例模式*

        实现只有一个BeanFactory的实例
        """
        if cls.__factory_bean is None:
            cls.__factory_bean = object.__new__(cls)
        return cls.__factory_bean


class FactoryBean(BeanFactory):
    """
    BeanFactory的子类

    通过add_bean方法，将bean实例添加到工厂
    """
    __factory_bean = None

    def __init__(self):
        if not self.contain_bean("factory_bean"):
            # 将自身 factory_bean 添加到工厂
            self.add_bean("factory_bean", self)

    def __new__(cls, *args, **kwargs):
        """
        *单例模式*

        实现只有一个FactoryBean的实例
        """
        if cls.__factory_bean is None:
            cls.__factory_bean = object.__new__(cls)
        return cls.__factory_bean

    def add_bean(self, name: str, bean):
        """
        将bean实例添加到工厂

        :param name: 名字
        :param bean: bean实例
        """
        self._beans[name] = bean

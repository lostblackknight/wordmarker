import os.path
from wordmarker.contexts import Context, YamlContext
from wordmarker.creatives import BeanFactory, FactoryBean


class WordMarkerContext(Context):
    """
    ::

        应用上下文，你可以从上下文中获取到：

        bean_factory：工厂里存放的bean实例的相关信息

        yaml_context：加载的yaml文件的相关信息

    """
    __word_marker_context = None
    __bean_factory = None  # getter方法获取
    __factory_bean = None  # 工厂获取
    __yaml_context = None  # getter方法获取
    __xml_context = None  # getter方法获取

    def __init__(self, resource):
        """
        :param resource: 路径必须为根路径或绝对路径
        """
        self.__resource = os.path.abspath(resource)
        if (not self.__factory_bean) and (not self.__bean_factory):  # 避免工厂多次初始化
            self._init()
        else:
            self.__init_other_context()

    def _init(self):
        self.__init_factory()
        self.__init_other_context()

    def __init_factory(self):
        """
        初始化工厂
        """
        self.__init_factory_bean()
        self.__init_bean_factory()

    def __init_other_context(self):
        """
        初始化其他上下文
        """
        self.__init_yaml_context()

    def __init_factory_bean(self):
        """
        初始化FactoryBean，用来添加bean实例
        """
        self.__factory_bean = FactoryBean()

    def __init_bean_factory(self):
        """
        初始化BeanFactory，用来获取bean的信息
        """
        self.__bean_factory = BeanFactory()

    def __init_yaml_context(self):
        """
        初始化yaml_context
        """
        # 1. 获取资源，然后加载资源
        self.__yaml_context = YamlContext(self.__resource)
        # 2. 将yaml_context添加到工厂
        self.__factory_bean.add_bean("yaml_context", self.__yaml_context)

    @property
    def bean_factory(self):
        """
        .. note::

            获取bean工厂

        :return: - bean工厂
        """
        return self.__bean_factory

    @property
    def yaml_context(self):
        """
        .. note::

            获取yaml文件的上下文

        :return: - yaml文件的上下文
        """
        return self.__yaml_context

    def __new__(cls, *args, **kwargs):
        if cls.__word_marker_context is None:
            cls.__word_marker_context = object.__new__(cls)
        return cls.__word_marker_context

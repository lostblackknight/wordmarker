import logging
import coloredlogs


class LoggerFactory(object):
    """
    ::

        logger工厂，获取logger对象
    """

    @staticmethod
    def get_logger(logger_name=None):
        """
        .. note::

            获取日志对象 ``logger``

        :param logger_name: ``logger`` 名字
        :return: - 日志对象 ``logger``
        """
        logger = logging.getLogger(logger_name)
        coloredlogs.install(logging.INFO)
        return logger


def log(fun):
    """
    .. note::

        装饰器，为类注入logger对象

    .. tip::

        在类的 ``__init__`` 方法上加上 ``@log`` ，可以通过类的 ``self._logger`` 获取到 ``logger`` 对象，来打印日志

        你也可以直接使用 ``LoggerFactory`` 获取 ``logger`` 对象，来打印日志

    .. error::

        只能放在类的 ``__init__`` 方法上，不能放在类上，放在类上会修改类的元类

        如果当前类是被继承或继承了某个类，会导致元类冲突的异常，所以目前只支持放在 ``__init__`` 方法上
    """

    def wrapper(self, *args):
        clazz_name = str(self.__class__)
        clazz_name = clazz_name.split("'")[1]
        logger: logging.Logger = LoggerFactory.get_logger(clazz_name)
        self._logger = logger
        return fun(self, *args)

    return wrapper

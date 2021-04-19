"""
:作者: 陈思祥

:时间: 2021年4月

:概述:
    当前模块使用工厂和生成器模式来管理对象的创建。

    1. ``wordmarker.creatives.factory``

        ::

            工厂模块。

    2. ``wordmarker.creatives.builder``

        ::

            生成器模块。
"""
from wordmarker.creatives.factory import BeanFactory
from wordmarker.creatives.factory import FactoryBean
from wordmarker.creatives.builder import AbstractBuilder

"""
:作者: 陈思祥

:时间: 2021年4月

:概述:
    当前模块用来加载资源。

    1. ``wordmarker.loaders.default_resource_loader``

        ::

            默认的资源加载器。

    2. ``wordmarker.loaders.yaml_resource_loader``

        ::

            yaml文件的资源加载器。

    3. ``wordmarker.loaders.resource_loader``

        ::

            资源加载器的抽象类。
"""
from wordmarker.loaders.default_resource_loader import DefaultResourceLoader
from wordmarker.loaders.yaml_resource_loader import YamlResourceLoader

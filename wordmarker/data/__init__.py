"""
:作者: 陈思祥

:时间: 2021年4月

:概述:
    当前模块用来处理数据和资源。

    1. ``wordmarker.data.resource``

        ::

            加载的资源，包含和资源相关的属性和判断。

    2. ``wordmarker.data.formatter``

        ::

            格式化数据，对某些数据进行处理。

"""
from wordmarker.data.resource import Resource
from wordmarker.data.formatter import SqlFormatter
from wordmarker.data.formatter import DocxFormatter

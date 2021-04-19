"""
:作者: 陈思祥

:时间: 2021年4月

:概述:
    当前模块包含整个应用的上下文。

    1. ``wordmarker.contexts.context``

        ::

            上下文的抽象类，所有的上下文都要继承它。

    2. ``wordmarker.contexts.system_context``

        ::

            系统上下文，获取和系统有关的属性。例如，路径分隔符，文件分隔符等。

    3. ``wordmarker.contexts.yaml_context``

        ::

            yaml文件的上下文，解析yaml文件。根据key值返回yaml文件中对应的value值。

    4. ``wordmarker.contexts.application_context``

        ::

            应用上下文，用来初始化工厂和其他的上下文。

            一般初始化，应用上下文WordMarkerContext来初始化整个应用。
"""
from wordmarker.contexts.context import Context
from wordmarker.contexts.system_context import SystemContext
from wordmarker.contexts.yaml_context import YamlContext
from wordmarker.contexts.application_context import WordMarkerContext

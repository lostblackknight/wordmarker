.. WordMarker documentation master file, created by
   sphinx-quickstart on Wed Apr 21 19:32:06 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

======================================
欢迎来到 WordMarker 的文档！
======================================

概述
=================

WordMarker是一个文档生成器，他提供了以下主要的功能。

1. 读写 ``.csv`` 文件。

   * 你可以使用 ``CsvTemplate`` 批量地读取 ``.csv`` 文件或者读取单个 ``.csv`` 文件转换为 ``DataFrame`` 类型的数据。
   * 你可以使用 ``CsvTemplate`` 将 ``DataFrame`` 类型的数据转换为 ``.csv`` 文件。
2. 读写数据库。

   * 你可以使用 ``PdbcTemplate`` 将 ``DataFrame`` 类型的数据写入到数据库中。
   * 你可以使用 ``PdbcTemplate`` 将数据库中的数据转换为 ``DataFrame`` 类型的数据。
3. 生成Word文档。

   * 你可以使用 ``WordTemplate`` 获取文本、图片、模板，通过模板生成固定格式的Word文档。

4. 其他。

   * 提供了一些实用的工具类，可以简化开发，它们位于 ``wordmarker.utils`` 模块中，使用方法可以参考API文档。

.. seealso::

   `DataFrame <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#>`_ 是pandas中的数据类型，
   请访问 `pandas官网 <https://pandas.pydata.org/>`_ ，了解更多信息。

快速入门
=================

.. toctree::
   :maxdepth: 4

   quickstart

参考文档
=================

* 敬请期待

API 文档
=================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. toctree::
   :maxdepth: 4

   wordmarker.contexts
   wordmarker.creatives
   wordmarker.data
   wordmarker.loaders
   wordmarker.templates
   wordmarker.utils

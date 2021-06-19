=================
快速入门
=================

在快速入门中，你将使用 ``wordmarker`` 构建一个示例项目，它包含了 ``wordmarker`` 的基本使用。你可以在 `GitHub <https://github.com/lostblackknight/wordmarker-example>`_ 上找到该示例。

环境搭建
=================

1. `Python <https://www.python.org/>`_ 的版本 ``>= 3.7``
2. `下载并安装 <https://pypi.org/project/wordmarker/>`_ 最新版的 ``wordmarker``
3. `安装 <https://www.postgresql.org/>`_ ``postgresql`` 数据库
4. 最好使用开发工具 `Pycharm <https://www.jetbrains.com/pycharm/>`_ 、`VsCode <https://code.visualstudio.com/>`_ 等

初始化项目
=================

1. 打开终端，进入项目的根目录，输入 ``wordmarker-quickstart`` 命令，按照提示完成项目的初始化

    ::

        欢迎使用 WordMarker 的脚手架，请按照提示完成项目的构建。
        -------------------------------------------------
        配置数据库
        -------------------------------------------------
        1. PostgreSQL
        2. MySql
        3. Oracle
        4. Microsoft
        数据库的类型，默认为 [1]: 1
        用户名，默认为 [postgres]:
        密码，默认为 [123456]: 123456
        主机，默认为 [localhost]:
        端口，默认为 [5432]:
        要连接的数据库: example
        -------------------------------------------------
        配置输入输出目录
        -------------------------------------------------
        是否启用默认的目录配置，默认为 [Y] [Y/n]: y
        成功创建data/in目录
        成功创建data/out目录
        成功创建template/in目录
        成功创建template/out目录
        成功创建img目录
        成功创建text目录

        成功构建项目 ^_^ !

2. 生成的目录结构如下

    ::

        ../wordmarker-example/
                             /data/in
                             /data/out
                             /img
                             /template/in
                             /template/out
                             /text
                             /config.yaml

3. ``config.yaml`` 文件中包含相关的配置

    .. code-block:: yaml

        # ======================================================================================================

        # ----------------------配置数据库信息
        #
        # 详细信息请查看 https://docs.sqlalchemy.org/en/14/core/engines.html
        # url:
        #    postgresql: "postgresql://username:password@localhost:5432/database"
        #    mysql: mysql+pymysql://username:password@localhost:3306/database
        # echo: 是否开启日志
        # encoding: 编码，默认utf-8
        # pool_size: 连接池大小
        # max_overflow: 连接的数量，以允许在连接池"溢出"
        # pool_recycle: 在给定的秒数过去之后，此设置将导致池回收连接。默认为-1。例如，设置为3600表示一小时后将回收连接
        # pool_timeout: 放弃从池中获得连接之前要等待的秒数
        # echo_pool: 是否开启日志
        pdbc:
          engine:
            url: postgresql://postgres:123456@localhost:5432/example
            echo: false
            encoding: utf-8
            pool_size: 5
            max_overflow: 10
            pool_recycle: -1
            pool_timeout: 30.0
            echo_pool: false

        # ======================================================================================================

        # ----------------------配置csv文件信息
        #
        # path: 文件的输入路径，可以是文件，也可以是目录
        #       路径分隔符为 '/' 或 '\'
        #       path的值为相对于当前yaml文件的路径
        # dir: 文件的输出目录
        #      路径分隔符为 '/' 或 '\'
        #      dir的值为相对于当前yaml文件的路径
        data:
          csv:
            input:
              path: data/in
            output:
              dir: data/out
          docx:
            input:
              path: template/in
            output:
              dir: template/out
          img:
            output:
              dir: img
          text:
            input:
              path: text

        # ======================================================================================================

4. 创建 ``main.py`` 文件，最终生成的目录如下

    ::

        ../wordmarker-example/
                             /data/in
                             /data/out
                             /img
                             /template/in
                             /template/out
                             /text
                             /config.yaml
                             /main.py

编写脚本
=================

1. 初始化 ``WordMarker`` 上下文和相关模板

    .. code-block:: python

        from wordmarker.contexts import WordMarkerContext
        from wordmarker.templates import CsvTemplate, PdbcTemplate, WordTemplate

        if __name__ == '__main__':
            # 初始化上下文
            WordMarkerContext("config.yaml")
            # 读写csv文件的模板
            csv_tpl = CsvTemplate()
            # 读写数据库的模板
            pdbc_tpl = PdbcTemplate()
            # 读写word文档的模板
            word_tpl = WordTemplate()

2. `下载 <https://github.com/lostblackknight/wordmarker-example/blob/master/data/in>`_ ``景气指数_加盐.csv`` 文件，将文件放入 ``../wordmarker-example/data/in`` 目录中，编写代码从配置中获取 ``.csv`` 文件，类型为 ``DataFrame``

    .. code-block:: python

        from wordmarker.contexts import WordMarkerContext
        from wordmarker.templates import CsvTemplate, PdbcTemplate, WordTemplate

        if __name__ == '__main__':
            # 初始化上下文
            WordMarkerContext("config.yaml")
            # 读写csv文件的模板
            csv_tpl = CsvTemplate()
            # 读写数据库的模板
            pdbc_tpl = PdbcTemplate()
            # 读写word文档的模板
            word_tpl = WordTemplate()

            # 从配置中获取.csv文件，类型为DataFrame
            csv_dict = csv_tpl.csv_to_df()
            prosperity_index_file = csv_dict['景气指数_加盐.csv']
            print(prosperity_index_file)

    ::

        输出结果

             起飞年  起飞星期      景气指数
        0    2015     1  89.57518
        1    2015    10  92.69366
        2    2015    11  92.43514
        3    2015    12  92.51584
        4    2015    13  92.45800
        ..    ...   ...       ...
        207  2018    53  85.67820
        208  2018     6  94.36436
        209  2018     7  94.22866
        210  2018     8  94.80134
        211  2018     9  94.37548

        [212 rows x 3 columns]

3. 创建数据库 ``example`` ，将 ``DataFrame`` 类型的数据写入数据库

    .. code-block:: python

        from wordmarker.contexts import WordMarkerContext
        from wordmarker.templates import CsvTemplate, PdbcTemplate, WordTemplate

        if __name__ == '__main__':
            # 初始化上下文
            WordMarkerContext("config.yaml")
            # 读写csv文件的模板
            csv_tpl = CsvTemplate()
            # 读写数据库的模板
            pdbc_tpl = PdbcTemplate()
            # 读写word文档的模板
            word_tpl = WordTemplate()

            # 从配置中获取.csv文件，类型为DataFrame
            csv_dict = csv_tpl.csv_to_df()
            prosperity_index_file = csv_dict['景气指数_加盐.csv']
            print(prosperity_index_file)

            # 将DataFrame类型的数据写入数据库
            pdbc_tpl.update_table(prosperity_index_file, "t_prosperity_index")

4. 从 ``example`` 数据库中获取数据，类型为 ``DataFrame``

    .. code-block:: python

        from wordmarker.contexts import WordMarkerContext
        from wordmarker.templates import CsvTemplate, PdbcTemplate, WordTemplate

        if __name__ == '__main__':
            # 初始化上下文
            WordMarkerContext("config.yaml")
            # 读写csv文件的模板
            csv_tpl = CsvTemplate()
            # 读写数据库的模板
            pdbc_tpl = PdbcTemplate()
            # 读写word文档的模板
            word_tpl = WordTemplate()

            # 从配置中获取.csv文件，类型为DataFrame
            csv_dict = csv_tpl.csv_to_df()
            prosperity_index_file = csv_dict['景气指数_加盐.csv']
            print(prosperity_index_file)

            # 将DataFrame类型的数据写入数据库
            pdbc_tpl.update_table(prosperity_index_file, "t_prosperity_index")

            # 从数据库中获取数据，类型为DataFrame
            prosperity_index_database = pdbc_tpl.query_table("t_prosperity_index")
            print(prosperity_index_database)

    ::

        输出结果

             起飞年  起飞星期      景气指数
        0    2015     1  89.57518
        1    2015    10  92.69366
        2    2015    11  92.43514
        3    2015    12  92.51584
        4    2015    13  92.45800
        ..    ...   ...       ...
        207  2018    53  85.67820
        208  2018     6  94.36436
        209  2018     7  94.22866
        210  2018     8  94.80134
        211  2018     9  94.37548

        [212 rows x 3 columns]

             起飞年  起飞星期      景气指数
        0    2015     1  89.57518
        1    2015    10  92.69366
        2    2015    11  92.43514
        3    2015    12  92.51584
        4    2015    13  92.45800
        ..    ...   ...       ...
        207  2018    53  85.67820
        208  2018     6  94.36436
        209  2018     7  94.22866
        210  2018     8  94.80134
        211  2018     9  94.37548

        [212 rows x 3 columns]

5. 将 ``DataFrame`` 类型的数据转换为 ``.csv`` 文件

    .. code-block:: python

        from wordmarker.contexts import WordMarkerContext
        from wordmarker.templates import CsvTemplate, PdbcTemplate, WordTemplate

        if __name__ == '__main__':
            # 初始化上下文
            WordMarkerContext("config.yaml")
            # 读写csv文件的模板
            csv_tpl = CsvTemplate()
            # 读写数据库的模板
            pdbc_tpl = PdbcTemplate()
            # 读写word文档的模板
            word_tpl = WordTemplate()

            # 从配置中获取.csv文件，类型为DataFrame
            csv_dict = csv_tpl.csv_to_df()
            prosperity_index_file = csv_dict['景气指数_加盐.csv']
            print(prosperity_index_file)

            # 将DataFrame类型的数据写入数据库
            pdbc_tpl.update_table(prosperity_index_file, "t_prosperity_index")

            # 从数据库中获取数据，类型为DataFrame
            prosperity_index_database = pdbc_tpl.query_table("t_prosperity_index")
            print(prosperity_index_database)

            # 将DataFrame类型的数据转换为.csv文件
            csv_tpl.df_to_csv({'景气指数_数据库.csv': prosperity_index_database})

    ::

        输出目录

        ../wordmarker-example/data/out/景气指数_数据库.csv

6. 编写 ``example.yaml`` 和 ``meta.yaml`` 文件，将这两个文件放在 ``../wordmarker-example/text/`` 目录下

    ``example.yaml``

    .. code-block:: yaml

        example:
          title: '景气指数'
          img_title: '图1 景气指数'
          explanation:
            - '2017年上半年民航全市场景气指数上涨：国内航线154，国际航线125，港澳台航线171。'
            - '2017年国内航线景气指数同比增幅放缓至0.40%，巿场稳步上升。'
            - '2017年国际航线景气指数增速上升，同比增幅与2016年放缓至0.40%，但春节峰值周景气指数超越2016年峰值，达到94.24，再创新高。'

    ``meta.yaml``

    .. code-block:: yaml

        meta:
          author: '{{ author }}'
          email: 'chensixiang1234@gamil.com'

7. 在 ``meta.yaml`` 文件中 ``meta.author`` 对应的值包含插值表达式。要对表达式赋值，需要创建 ``AbstractConverter`` 类的实现类，并且创建实现类的对象

    .. code-block:: python

        from wordmarker.contexts import WordMarkerContext
        from wordmarker.templates import CsvTemplate, PdbcTemplate, WordTemplate, AbstractConverter

        class TextConverter(AbstractConverter):
            def __init__(self, word_tpl_: WordTemplate):
                super().__init__(word_tpl_)

            @staticmethod
            def author():
                return 'chensixiang'

        if __name__ == '__main__':
            # 初始化上下文
            WordMarkerContext("config.yaml")
            # 读写csv文件的模板
            csv_tpl = CsvTemplate()
            # 读写数据库的模板
            pdbc_tpl = PdbcTemplate()
            # 读写word文档的模板
            word_tpl = WordTemplate()

            # 从配置中获取.csv文件，类型为DataFrame
            csv_dict = csv_tpl.csv_to_df()
            prosperity_index_file = csv_dict['景气指数_加盐.csv']
            print(prosperity_index_file)

            # 将DataFrame类型的数据写入数据库
            pdbc_tpl.update_table(prosperity_index_file, "t_prosperity_index")

            # 从数据库中获取数据，类型为DataFrame
            prosperity_index_database = pdbc_tpl.query_table("t_prosperity_index")
            print(prosperity_index_database)

            # 将DataFrame类型的数据转换为.csv文件
            csv_tpl.df_to_csv({'景气指数_数据库.csv': prosperity_index_database})

            # 创建TextConverter对象，它继承了AbstractConverter，可以将yaml模板中的插值表达式进行转换
            text = TextConverter(word_tpl)

8. `下载 <https://github.com/lostblackknight/wordmarker-example/tree/master/template/in>`_ ``default_tpl.docx`` 文件，将文件放入 ``../wordmarker-example/template/in`` 目录中，`下载 <https://github.com/lostblackknight/wordmarker-example/tree/master/img>`_ ``景气指数.png`` 文件，将文件放入 ``../wordmarker-example/img`` 目录中，并修改 ``config.yaml`` 中的 ``data.docx.input.path`` 的配置，以及编写 ``content`` 字典

    ``config.yaml``

    .. code-block:: yaml

        # ======================================================================================================

        # ----------------------配置数据库信息
        #
        # 详细信息请查看 https://docs.sqlalchemy.org/en/14/core/engines.html
        # url:
        #    postgresql: "postgresql://username:password@localhost:5432/database"
        #    mysql: mysql+pymysql://username:password@localhost:3306/database
        # echo: 是否开启日志
        # encoding: 编码，默认utf-8
        # pool_size: 连接池大小
        # max_overflow: 连接的数量，以允许在连接池"溢出"
        # pool_recycle: 在给定的秒数过去之后，此设置将导致池回收连接。默认为-1。例如，设置为3600表示一小时后将回收连接
        # pool_timeout: 放弃从池中获得连接之前要等待的秒数
        # echo_pool: 是否开启日志
        pdbc:
          engine:
            url: postgresql://postgres:123456@localhost:5432/example
            echo: false
            encoding: utf-8
            pool_size: 5
            max_overflow: 10
            pool_recycle: -1
            pool_timeout: 30.0
            echo_pool: false

        # ======================================================================================================

        # ----------------------配置csv文件信息
        #
        # path: 文件的输入路径，可以是文件，也可以是目录
        #       路径分隔符为 '/' 或 '\'
        #       path的值为相对于当前yaml文件的路径
        # dir: 文件的输出目录
        #      路径分隔符为 '/' 或 '\'
        #      dir的值为相对于当前yaml文件的路径
        data:
          csv:
            input:
              path: data/in
            output:
              dir: data/out
          docx:
            input:
              path: template/in/default_tpl.docx
            output:
              dir: template/out
          img:
            output:
              dir: img
          text:
            input:
              path: text

        # ======================================================================================================

    .. code-block:: python

        from wordmarker.contexts import WordMarkerContext
        from wordmarker.templates import CsvTemplate, PdbcTemplate, WordTemplate, AbstractConverter
        from docxtpl import InlineImage
        from docx.shared import Mm


        class TextConverter(AbstractConverter):
            def __init__(self, word_tpl_: WordTemplate):
                super().__init__(word_tpl_)

            @staticmethod
            def author():
                return 'chensixiang'

        if __name__ == '__main__':
            # 初始化上下文
            WordMarkerContext("config.yaml")
            # 读写csv文件的模板
            csv_tpl = CsvTemplate()
            # 读写数据库的模板
            pdbc_tpl = PdbcTemplate()
            # 读写word文档的模板
            word_tpl = WordTemplate()

            # 从配置中获取.csv文件，类型为DataFrame
            csv_dict = csv_tpl.csv_to_df()
            prosperity_index_file = csv_dict['景气指数_加盐.csv']
            print(prosperity_index_file)

            # 将DataFrame类型的数据写入数据库
            pdbc_tpl.update_table(prosperity_index_file, "t_prosperity_index")

            # 从数据库中获取数据，类型为DataFrame
            prosperity_index_database = pdbc_tpl.query_table("t_prosperity_index")
            print(prosperity_index_database)

            # 将DataFrame类型的数据转换为.csv文件
            csv_tpl.df_to_csv({'景气指数_数据库.csv': prosperity_index_database})

            # 创建TextConverter对象，它继承了AbstractConverter，可以将yaml模板中的插值表达式进行转换
            text = TextConverter(word_tpl)

            content = {
                # 直接赋值
                'title': '景气指数',
                # 从example.yaml模板中获取值
                'img_title': word_tpl.get_value("example.img_title"),
                # 图片
                'img': InlineImage(word_tpl.tpl, word_tpl.get_img_file('景气指数.png'),
                                   width=Mm(100)),
                # 从example.yaml模板中获取值
                'explanation': word_tpl.get_value("example.explanation"),
                # 从meta.yaml模板中获取将插值表达式进行转换后的值
                'author': text.get_value("meta.author"),
                # 从meta.yaml模板中获取值
                'email': word_tpl.get_value("meta.email"),
            }

9. 添加 ``content`` 到总的上下文中，并输出word文档

    .. code-block:: python

        from wordmarker.contexts import WordMarkerContext
        from wordmarker.templates import CsvTemplate, PdbcTemplate, WordTemplate, AbstractConverter
        from docxtpl import InlineImage
        from docx.shared import Mm


        class TextConverter(AbstractConverter):
            def __init__(self, word_tpl_: WordTemplate):
                super().__init__(word_tpl_)

            @staticmethod
            def author():
                return 'chensixiang'

        if __name__ == '__main__':
            # 初始化上下文
            WordMarkerContext("config.yaml")
            # 读写csv文件的模板
            csv_tpl = CsvTemplate()
            # 读写数据库的模板
            pdbc_tpl = PdbcTemplate()
            # 读写word文档的模板
            word_tpl = WordTemplate()

            # 从配置中获取.csv文件，类型为DataFrame
            csv_dict = csv_tpl.csv_to_df()
            prosperity_index_file = csv_dict['景气指数_加盐.csv']
            print(prosperity_index_file)

            # 将DataFrame类型的数据写入数据库
            pdbc_tpl.update_table(prosperity_index_file, "t_prosperity_index")

            # 从数据库中获取数据，类型为DataFrame
            prosperity_index_database = pdbc_tpl.query_table("t_prosperity_index")
            print(prosperity_index_database)

            # 将DataFrame类型的数据转换为.csv文件
            csv_tpl.df_to_csv({'景气指数_数据库.csv': prosperity_index_database})

            # 创建TextConverter对象，它继承了AbstractConverter，可以将yaml模板中的插值表达式进行转换
            text = TextConverter(word_tpl)

            content = {
                # 直接赋值
                'title': '景气指数',
                # 从example.yaml模板中获取值
                'img_title': word_tpl.get_value("example.img_title"),
                # 图片
                'img': InlineImage(word_tpl.tpl, word_tpl.get_img_file('景气指数.png'),
                                   width=Mm(100)),
                # 从example.yaml模板中获取值
                'explanation': word_tpl.get_value("example.explanation"),
                # 从meta.yaml模板中获取将插值表达式进行转换后的值
                'author': text.get_value("meta.author"),
                # 从meta.yaml模板中获取值
                'email': word_tpl.get_value("meta.email"),
            }

            # 添加content到总的上下文中
            word_tpl.append(content)
            # 输出word文档
            word_tpl.build("example.docx")

    ::

        输出目录

        ../wordmarker-example/template/out/
                                          /example/
                                                  /img/景气指数.png
                                                  /example.docx

10. `下载 <https://github.com/lostblackknight/wordmarker-example/tree/master/template/out/example>`_ ``example.docx`` 文件


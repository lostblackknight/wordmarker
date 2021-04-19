"""
:作者: 陈思祥

:时间: 2021年4月

:概述:
    当前模块是WordMarker的核心模块，可以读写csv文件，操纵数据库，读写docx文件等。

    1. ``wordmarker.templates.pdbc_template``

        ::

            操纵数据库的模板。

    2. ``wordmarker.templates.csv_template``

        ::

            读写csv文件的模板。

    3. ``wordmarker.templates.word_template``

        ::

            读写docx文件的模板。
"""
from wordmarker.templates.pdbc_template import PdbcTemplate
from wordmarker.templates.pdbc_template import PdbcHelper
from wordmarker.templates.csv_template import CsvTemplate
from wordmarker.templates.csv_template import CsvHelper
from wordmarker.templates.word_template import WordTemplate
from wordmarker.templates.word_template import ImgHelper, DocxHelper

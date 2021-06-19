import logging
import os
import shutil
from docxtpl import DocxTemplate, R
from wordmarker.contexts import YamlContext, SystemContext
from wordmarker.creatives import FactoryBean, AbstractBuilder
from wordmarker.loaders import DefaultResourceLoader
from wordmarker.utils import PathUtils, log


class DocxHelper(DefaultResourceLoader):
    """
    ::

        通过读取配置文件，获取docx文件模板的相关信息
    """
    __docx_helper = None

    def __init__(self):
        super().__init__()
        self.__yaml_context: YamlContext = FactoryBean().get_bean("yaml_context")
        self._docx_in_path = self._get_docx_in_path()
        self._docx_out_path = self._get_docx_out_path()
        self._docx = self._get_docx()

    def _get_docx_in_path(self):
        """
        .. note::

            通过读取yaml文件的 ``data.docx.input.path`` 属性，获取输入的docx文件或目录的绝对路径

        :return: - docx文件或目录的绝对路径
        """
        prop = "data.docx.input.path"
        value = self.__yaml_context.get_value(prop)
        docx_in_path = PathUtils(self.__yaml_context.path, value).get_relative_path()
        self._docx_in_path = docx_in_path
        return docx_in_path

    def _get_docx_out_path(self):
        """
        .. note::

            通过读取yaml文件的 ``data.docx.output.dir`` 属性，获取输出的docx目录的绝对路径

        :return: - docx目录的绝对路径
        """
        prop = "data.docx.output.dir"
        value = self.__yaml_context.get_value(prop)
        return PathUtils(self.__yaml_context.path, value).get_relative_path()

    def _get_docx(self):
        """
        .. note::

            获取docx文件的绝对路径

        :return: - yaml文件中 ``data.docx.input.path`` 是目录，返回当前目录下docx文件的绝对路径

                 - yaml文件中 ``data.docx.input.path`` 是文件，返回docx文件的绝对路径
        """
        docx = self.get_resource(self._docx_in_path).get_file()
        if not self.get_resource(self._docx_in_path).is_file():
            # 是目录
            docx = PathUtils.filter_file(docx, ['.docx'])
        else:
            # 是文件
            docx = PathUtils.filter_file(docx, ['.docx'])[0]
        return docx

    def get_docx_file_name(self):
        """
        .. note::

            获取docx文件的文件名

        :return: - 是docx文件，返回文件的名字

                 - 是目录，返回当前目录下的所有docx文件的文件名
        """
        docx = self._docx
        if type(docx) is list:
            temp_list = []
            for item in docx:
                temp_list.append(os.path.split(item)[1])
            return temp_list
        else:
            return os.path.split(docx)[1]

    @property
    def docx_in_path(self):
        """
        .. note::

            通过读取yaml文件的 ``data.docx.input.path`` 属性，获取输入的docx文件或目录的绝对路径

        :return: - docx文件或目录的绝对路径
        """
        return self._docx_in_path

    @property
    def docx_out_path(self):
        """
        .. note::

            通过读取yaml文件的 ``data.docx.output.dir`` 属性，获取输出的docx目录的绝对路径

        :return: - docx目录的绝对路径
        """
        return self._docx_out_path

    @property
    def docx(self):
        """
        .. note::

            获取docx文件的绝对路径

        :return: - yaml文件中 ``data.docx.input.path`` 是目录，返回当前目录下docx文件的绝对路径

                 - yaml文件中 ``data.docx.input.path`` 是文件，返回docx文件的绝对路径
        """
        return self._docx

    def __new__(cls, *args, **kwargs):
        if cls.__docx_helper is None:
            cls.__docx_helper = object.__new__(cls)
        return cls.__docx_helper


class ImgHelper(SystemContext):
    """
    ::

        通过读取配置文件，获取img文件的相关信息
    """
    __img_helper = None

    def __init__(self):
        super().__init__()
        self.__yaml_context: YamlContext = FactoryBean().get_bean("yaml_context")
        self.__img_out_path = self._get_img_out_path()

    def _get_img_out_path(self):
        prop = "data.img.output.dir"
        value = self.__yaml_context.get_value(prop)
        return PathUtils(self.__yaml_context.path, value).get_relative_path()

    def get_img_file(self, img_name):
        """
        .. note::

            根据图片的名字，获取图片的绝对路径

        .. warning::

            必须先将图片输出到输出目录下，才能获取到

        :param img_name: 图片的名字
        :return: - 图片的绝对路径
        """
        final_path = self.__img_out_path + self.path_separator + img_name
        return final_path

    @property
    def img_out_path(self):
        """
        .. note::

            通过读取yaml文件的 ``data.img.output.dir`` 属性，获取输出的img目录的绝对路径

        :return: - img目录的绝对路径
        """
        return self.__img_out_path

    def clear_img(self):
        """
        .. note::

            清除 ``data.img.output.dir`` 属性对应的img的输出目录下的所有文件和目录

        """
        if os.path.exists(self.__img_out_path):
            shutil.rmtree(self.__img_out_path)
            os.mkdir(self.__img_out_path)

    def __new__(cls, *args, **kwargs):
        if cls.__img_helper is None:
            cls.__img_helper = object.__new__(cls)
        return cls.__img_helper


class TextHelper:
    """
    ::

        通过读取配置文件，获取文本yaml文件的相关信息
    """
    __text_helper = None

    def __init__(self):
        super().__init__()
        self.__yaml_context: YamlContext = FactoryBean().get_bean("yaml_context")
        self.__text_in_path = self._get_text_in_path()
        self.__text_context = YamlContext(self.text_in_path)
        self.__yaml_singleton = {}

    def _get_text_in_path(self):
        prop = "data.text.input.path"
        value = self.__yaml_context.get_value(prop)
        return PathUtils(self.__yaml_context.path, value).get_relative_path()

    @property
    def text_in_path(self):
        """
        .. note::

            通过读取yaml文件的 ``data.text.input.path`` 属性，获取输入的文本yaml文件的绝对路径

        :return: - 文本yaml文件的绝对路径
        """
        return self.__text_in_path

    def get_value(self, prop):
        """
        .. note::

            从yaml字典中，根据属性获取对应的值

            加载多个yaml文件，排在后面的文件里的值，会覆盖前面的文件里的值

        :param prop: 属性，用 ``.`` 分隔，例如，``pdbc.engine.url``
        :return: - yaml字典中对应的值
        """
        return self.__text_context.get_value(prop)

    def get_yaml(self) -> dict:
        """
        .. note::

            获取从yaml文件中读取的数据，类型为dict

        :return: - path为文件，返回一个字典，内容为yaml文件的内容

                 - path为目录，返回一个嵌套的字典

                    - key为yaml文件的绝对路径

                    - value为yaml文件的内容，是一个字典
        """
        return self.__text_context.get_yaml()

    def get_yaml_singleton(self):
        """
        .. note::

            获取从 ``data.text.input.path`` 属性中对应的路径下所有yaml文件中的数据，类型为dict

            加载多个yaml文件，排在后面的文件里的值，会覆盖前面的文件里的值

        :return: - 返回一个字典，内容为所有yaml文件的内容
        """
        for i in self.get_yaml().values():
            self.__yaml_singleton.update(i)
        return self.__yaml_singleton

    def get_yaml_singleton_str(self):
        """
        .. note::

            获取从 ``data.text.input.path`` 属性中对应的路径下所有yaml文件中的数据，类型为str，内容为一个字典

            加载多个yaml文件，排在后面的文件里的值，会覆盖前面的文件里的值

        :return: - 返回一个字符串，内容为一个字典，内容为所有yaml文件的内容
        """
        return str(self.get_yaml_singleton())

    def __new__(cls, *args, **kwargs):
        if cls.__text_helper is None:
            cls.__text_helper = object.__new__(cls)
        return cls.__text_helper


class WordTemplate(AbstractBuilder, TextHelper, ImgHelper, DocxHelper):
    """
    ::

        操作docx文件的模板
    """

    @log
    def __init__(self, tpl_name=None):
        super().__init__()
        self.content = {'page_break': R('\f')}
        self.__tpl_name = tpl_name
        self.__tpl = DocxTemplate(self.__get_tpl_name_abs())

    def __get_tpl_name_abs(self):
        if type(self._get_docx()) is list:
            if self.__tpl_name is None:
                self._logger: logging.Logger
                self._logger.error("请输入模板的文件名")
            else:
                for i in self.get_docx_file_name():
                    if self.__tpl_name == i:
                        for j in self._get_docx():
                            if self.__tpl_name == os.path.split(j)[1]:
                                return j
                    else:
                        self._logger.error("模板的文件名不正确")
                        break
        else:
            return self._docx

    def append(self, content):
        """
        .. note::

            添加其他的content到全局的content中

        :param content: 其他的content，类型是 ``dict``
        :return: - self
        """
        self.content.update(content)
        return self

    def build(self, file_name=None):
        """
        .. note::

            创建docx文件

        :param file_name: docx文件的文件名
        """
        if file_name:
            self.__tpl.render(self.content)
            path = self.docx_out_path + self.path_separator + os.path.splitext(file_name)[0]
            if os.path.exists(path):
                shutil.rmtree(path)
            os.mkdir(path)
            img_path = path + self.path_separator + 'img'
            if os.path.exists(img_path):
                shutil.rmtree(img_path)
            shutil.copytree(self.img_out_path, img_path)
            self.__tpl.save(path + self.path_separator + file_name)
        else:
            self._logger: logging.Logger
            self._logger.error('请输入输出的docx文件的文件名')

    @property
    def tpl(self):
        """
        .. note::

            获取 ``DocxTemplate`` 对象，

        .. tip::

            ``DocxTemplate`` 对象的详细信息，请访问 `python-docx-template的文档 <https://docxtpl.readthedocs.io/>`_

        :return: - ``DocxTemplate`` 对象
        """
        return self.__tpl

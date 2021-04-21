import os
from abc import ABCMeta, abstractmethod
from wordmarker.contexts import YamlContext, SystemContext
from wordmarker.creatives import FactoryBean, AbstractBuilder
from wordmarker.loaders import DefaultResourceLoader
from wordmarker.utils import PathUtils


class DocxOperations(metaclass=ABCMeta):
    """
    ::

        docx文件的相关操作的抽象类
    """
    pass


class DocxHelper(DefaultResourceLoader):
    """
    ::

        通过读取配置文件，获取docx文件模板的相关信息
    """
    __docx_helper = None

    def __init__(self):
        super().__init__()
        self.__docx = None
        self.__yaml_context: YamlContext = FactoryBean().get_bean("yaml_context")
        self._docx_in_path = self._get_docx_in_path()
        self._docx_out_path = self._get_docx_out_path()

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

    def get_docx(self):
        """
        .. note::

            获取docx文件的绝对路径

        :return: - yaml文件中 ``data.docx.input.path`` 是目录，再返回当前目录下docx文件的绝对路径

                 - yaml文件中 ``data.docx.input.path`` 是文件，返回docx文件的绝对路径
        """
        docx = self.get_resource(self._docx_in_path).get_file()
        if not self.get_resource(self._docx_in_path).is_file():
            # 是目录
            docx = PathUtils.filter_file(docx, ['.docx'])
        else:
            # 是文件
            docx = PathUtils.filter_file(docx, ['.docx'])[0]
        self.__docx = docx
        return docx

    def get_docx_file_name(self):
        """
        .. note::

            获取docx文件的文件名

        :return: - 是docx文件，返回文件的名字
                 - 是目录，返回当前目录下的所有docx文件的文件名
        """
        docx = self.__docx
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

    def __new__(cls, *args, **kwargs):
        if cls.__img_helper is None:
            cls.__img_helper = object.__new__(cls)
        return cls.__img_helper


class WordTemplate(DocxHelper, AbstractBuilder, ImgHelper):
    """
    ::

        操作docx文件的模板
    """

    def __init__(self):
        super().__init__()

    def append(self, *args, **kwargs):
        pass

    def build(self):
        pass

    def append_img(self):
        pass

    def append_text(self):
        pass

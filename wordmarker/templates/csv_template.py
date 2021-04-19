import csv
from abc import ABCMeta, abstractmethod
from logging import Logger
from typing import Union, List, Dict, Optional, Sequence
import pandas as pd
from pandas import DataFrame, Series
from pandas._libs import lib
from pandas._typing import StorageOptions, Label, IndexLabel, CompressionOptions
from pandas.core.generic import bool_t
from pandas.io.parsers import _c_parser_defaults, TextFileReader
from wordmarker.contexts import YamlContext, SystemContext
from wordmarker.creatives import FactoryBean
from wordmarker.loaders import DefaultResourceLoader
from wordmarker.utils import log, PathUtils


class CsvOperations(metaclass=ABCMeta):
    """
    ::

        csv文件的相关操作的抽象类
    """

    @abstractmethod
    def csv_to_df(self):
        """
        .. note::

            将csv文件转换为 ``DataFrame``

        :return: - 数据框
        """
        pass

    @abstractmethod
    def df_to_csv(self, *args, **kwargs):
        """
        .. note::

            将 ``DataFrame`` 转换为csv文件

        """
        pass


class CsvHelper(DefaultResourceLoader, SystemContext):
    """
    ::

        通过读取配置文件，获取csv文件的相关信息
    """
    __csv_helper = None

    @log
    def __init__(self):
        super().__init__()
        self.__yaml_context: YamlContext = FactoryBean().get_bean("yaml_context")

    def get_csv_in_path(self):
        """
        .. note::

            通过读取yaml文件的 ``data.csv.in.path`` 属性，获取输入的csv文件或目录的绝对路径

        :return: - csv文件或目录的绝对路径
        """
        prop = "data.csv.input.path"
        value = self.__yaml_context.get_value(prop)
        return PathUtils(self.__yaml_context.path, value).get_relative_path()

    def get_csv_out_path(self):
        """
        .. note::

            通过读取yaml文件的 ``data.csv.output.dir`` 属性，获取输出的csv的目录的绝对路径

        :return: - csv目录的绝对路径
        """
        prop = "data.csv.output.dir"
        value = self.__yaml_context.get_value(prop)
        return PathUtils(self.__yaml_context.path, value).get_relative_path()

    def get_csv(self):
        """
        .. note::

            获取csv文件的绝对路径

        :return: - yaml文件中 ``data.csv.input.path`` 是目录，返回当前目录下的所有csv文件的绝对路径

                 - yaml文件中 ``data.csv.input.path`` 是文件，返回当前文件的绝对路径
        """
        return self.get_resource(self.get_csv_in_path()).get_file()

    def get_csv_file_name(self):
        """
        .. note::

            获取csv文件的文件名

        :return: - 是文件，返回文件的名字

                 - 是目录，返回当前目录下的所有文件的文件名
        """
        return self.get_resource(self.get_csv_in_path()).get_file_name()

    def __new__(cls, *args, **kwargs):
        if cls.__csv_helper is None:
            cls.__csv_helper = object.__new__(cls)
        return cls.__csv_helper


class CsvTemplate(CsvOperations, CsvHelper):
    """
    ::

        操作csv文件的模板
    """

    @log
    def __init__(self):
        super().__init__()

    def csv_to_df(self,
                  sep=lib.no_default,
                  delimiter=None,
                  # Column and Index Locations and Names
                  header="infer",
                  names=None,
                  index_col=0,
                  usecols=None,
                  squeeze=False,
                  prefix=None,
                  mangle_dupe_cols=True,
                  # General Parsing Configuration
                  dtype=None,
                  engine=None,
                  converters=None,
                  true_values=None,
                  false_values=None,
                  skipinitialspace=False,
                  skiprows=None,
                  skipfooter=0,
                  nrows=None,
                  # NA and Missing Data Handling
                  na_values=None,
                  keep_default_na=True,
                  na_filter=True,
                  verbose=False,
                  skip_blank_lines=True,
                  # Datetime Handling
                  parse_dates=False,
                  infer_datetime_format=False,
                  keep_date_col=False,
                  date_parser=None,
                  dayfirst=False,
                  cache_dates=True,
                  # Iteration
                  iterator=False,
                  chunksize=None,
                  # Quoting, Compression, and File Format
                  compression="infer",
                  thousands=None,
                  decimal: str = ".",
                  lineterminator=None,
                  quotechar='"',
                  quoting=csv.QUOTE_MINIMAL,
                  doublequote=True,
                  escapechar=None,
                  comment=None,
                  encoding=None,
                  dialect=None,
                  # Error Handling
                  error_bad_lines=True,
                  warn_bad_lines=True,
                  # Internal
                  delim_whitespace=False,
                  low_memory=_c_parser_defaults["low_memory"],
                  memory_map=False,
                  float_precision=None,
                  storage_options: StorageOptions = None,
                  ) -> Union[Union[TextFileReader, Series, DataFrame, None],
                             Dict[str, Union[TextFileReader, Series, DataFrame, None]]]:
        """
        .. note::

            从yaml配置中读取csv文件，转换为 ``pandas`` 的 ``DataFrame``

        .. tip::

            `csv_to_df的参数详情 <https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html#pandas.read_csv>`_ ，
            请访问 `pandas官网`_ ，了解更多信息

        :return: - 多个csv文件，返回一个 ``DataFrame`` 的字典

                    - key为文件名
                    - value为 ``DataFrame``
                 - 一个csv文件，返回一个 ``DataFrame``
        """
        csv_file = self.get_csv()
        csv_dict = {}
        if type(csv_file) is list:
            index = 0
            for i in csv_file:
                csv_dict[self.get_csv_file_name()[index]] = pd.read_csv(i,
                                                                        sep=sep,
                                                                        delimiter=delimiter,
                                                                        header=header,
                                                                        names=names,
                                                                        index_col=index_col,
                                                                        usecols=usecols,
                                                                        squeeze=squeeze,
                                                                        prefix=prefix,
                                                                        mangle_dupe_cols=mangle_dupe_cols,
                                                                        dtype=dtype,
                                                                        engine=engine,
                                                                        converters=converters,
                                                                        true_values=true_values,
                                                                        false_values=false_values,
                                                                        skipinitialspace=skipinitialspace,
                                                                        skiprows=skiprows,
                                                                        skipfooter=skipfooter,
                                                                        nrows=nrows,
                                                                        na_values=na_values,
                                                                        keep_default_na=keep_default_na,
                                                                        na_filter=na_filter,
                                                                        verbose=verbose,
                                                                        skip_blank_lines=skip_blank_lines,
                                                                        parse_dates=parse_dates,
                                                                        infer_datetime_format=infer_datetime_format,
                                                                        keep_date_col=keep_date_col,
                                                                        date_parser=date_parser,
                                                                        dayfirst=dayfirst,
                                                                        cache_dates=cache_dates,
                                                                        iterator=iterator,
                                                                        chunksize=chunksize,
                                                                        compression=compression,
                                                                        thousands=thousands,
                                                                        decimal=decimal,
                                                                        lineterminator=lineterminator,
                                                                        quotechar=quotechar,
                                                                        quoting=quoting,
                                                                        doublequote=doublequote,
                                                                        escapechar=escapechar,
                                                                        comment=comment,
                                                                        encoding=encoding,
                                                                        dialect=dialect,
                                                                        error_bad_lines=error_bad_lines,
                                                                        warn_bad_lines=warn_bad_lines,
                                                                        delim_whitespace=delim_whitespace,
                                                                        low_memory=low_memory,
                                                                        memory_map=memory_map,
                                                                        float_precision=float_precision,
                                                                        storage_options=storage_options)
                index += 1
            return csv_dict
        else:
            return pd.read_csv(csv_file,
                               sep=sep,
                               delimiter=delimiter,
                               header=header,
                               names=names,
                               index_col=index_col,
                               usecols=usecols,
                               squeeze=squeeze,
                               prefix=prefix,
                               mangle_dupe_cols=mangle_dupe_cols,
                               dtype=dtype,
                               engine=engine,
                               converters=converters,
                               true_values=true_values,
                               false_values=false_values,
                               skipinitialspace=skipinitialspace,
                               skiprows=skiprows,
                               skipfooter=skipfooter,
                               nrows=nrows,
                               na_values=na_values,
                               keep_default_na=keep_default_na,
                               na_filter=na_filter,
                               verbose=verbose,
                               skip_blank_lines=skip_blank_lines,
                               parse_dates=parse_dates,
                               infer_datetime_format=infer_datetime_format,
                               keep_date_col=keep_date_col,
                               date_parser=date_parser,
                               dayfirst=dayfirst,
                               cache_dates=cache_dates,
                               iterator=iterator,
                               chunksize=chunksize,
                               compression=compression,
                               thousands=thousands,
                               decimal=decimal,
                               lineterminator=lineterminator,
                               quotechar=quotechar,
                               quoting=quoting,
                               doublequote=doublequote,
                               escapechar=escapechar,
                               comment=comment,
                               encoding=encoding,
                               dialect=dialect,
                               error_bad_lines=error_bad_lines,
                               warn_bad_lines=warn_bad_lines,
                               delim_whitespace=delim_whitespace,
                               low_memory=low_memory,
                               memory_map=memory_map,
                               float_precision=float_precision,
                               storage_options=storage_options
                               )

    def df_to_csv(self,
                  data_dict: Dict[str, DataFrame],
                  sep: str = ",",
                  na_rep: str = "",
                  float_format: Optional[str] = None,
                  columns: Optional[Sequence[Label]] = None,
                  header: Union[bool_t, List[str]] = True,
                  index: bool_t = True,
                  index_label: Optional[IndexLabel] = None,
                  mode: str = "w",
                  encoding: Optional[str] = None,
                  compression: CompressionOptions = "infer",
                  quoting: Optional[int] = None,
                  quotechar: str = '"',
                  line_terminator: Optional[str] = None,
                  chunksize: Optional[int] = None,
                  date_format: Optional[str] = None,
                  doublequote: bool_t = True,
                  escapechar: Optional[str] = None,
                  decimal: str = ".",
                  errors: str = "strict",
                  storage_options: StorageOptions = None,
                  ):
        """
        .. note::

            将一个或多个 ``DataFrame`` 转换成csv文件，输出到指定文件夹

        .. tip::

            `df_to_csv的参数详情 <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html?highlight=to_csv#pandas.DataFrame.to_csv>`_ ，
            请访问 `pandas官网`_ ，了解更多信息

        :param data_dict: 由 ``DataFrame`` 组成的字典，key为输出的文件名，value为 ``DataFrame``
        """
        d = self.get_csv_out_path()

        if type(data_dict) is dict:
            file_name_list = []
            for key in data_dict.keys():
                file_name_list.append(key)

            data_list = []

            for value in data_dict.values():
                data_list.append(value)

            idx = 0
            for value in data_list:
                value.to_csv(d + self.path_separator + file_name_list[idx],
                             sep=sep,
                             na_rep=na_rep,
                             float_format=float_format,
                             columns=columns,
                             header=header,
                             index=index,
                             index_label=index_label,
                             mode=mode,
                             encoding=encoding,
                             compression=compression,
                             quoting=quoting,
                             quotechar=quotechar,
                             line_terminator=line_terminator,
                             chunksize=chunksize,
                             date_format=date_format,
                             doublequote=doublequote,
                             escapechar=escapechar,
                             decimal=decimal,
                             errors=errors,
                             storage_options=storage_options
                             )
                idx += 1
            self._logger: Logger
            self._logger.info("csv文件输出成功")
        else:
            self._logger.error("输入参数不正确")

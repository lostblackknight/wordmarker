import pandas as pd
import sqlalchemy as sa
from abc import ABCMeta, abstractmethod
from copy import deepcopy
from logging import Logger
from typing import Iterator, Union, Optional
from pandas import DataFrame
from pandas.core.generic import bool_t
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.exc import ArgumentError
from wordmarker.contexts import YamlContext
from wordmarker.creatives import FactoryBean
from wordmarker.data.formatter import SqlFormatter
from wordmarker.utils import log


class PdbcOperations(metaclass=ABCMeta):
    """
    数据库的相关操作
    """

    @abstractmethod
    def execute(self, sql):
        pass

    @abstractmethod
    def update(self, sql):
        pass

    @abstractmethod
    def query(self, sql):
        pass


class PdbcHelper:
    """
    通过读取配置文件获取数据库的信息，进而建立连接
    """
    __engine_dict = {}  # sqlalchemy.create_engine方法中传入的值的字典
    __pdbc_helper = None

    @log
    def __init__(self):
        self.__yaml_context: YamlContext = FactoryBean().get_bean("yaml_context")
        self._get_url()
        self._get_echo()
        self._get_encoding()
        self._get_pool_size()
        self._get_pool_timeout()
        self._get_pool_recycle()
        self._get_max_overflow()
        self._get_echo_pool()
        self._engine = None
        self.set_engine()

    def _get_url(self):
        """
        获取配置文件中url的值
        """
        prop = "pdbc.engine.url"
        value = self.__yaml_context.get_value(prop)
        prop = prop.split('.')[2]
        self.__engine_dict[prop] = value
        return value

    def _get_echo(self):
        """
        获取配置文件中echo的值
        """
        prop = "pdbc.engine.echo"
        value = self.__yaml_context.get_value(prop)
        prop = prop.split('.')[2]
        self.__engine_dict[prop] = value
        return value

    def _get_encoding(self):
        """
        获取配置文件中encoding的值
        """
        prop = "pdbc.engine.encoding"
        value = self.__yaml_context.get_value(prop)
        prop = prop.split('.')[2]
        self.__engine_dict[prop] = value
        return value

    def _get_pool_size(self):
        """
        获取配置文件中pool_size的值
        """
        prop = "pdbc.engine.pool_size"
        value = self.__yaml_context.get_value(prop)
        prop = prop.split('.')[2]
        self.__engine_dict[prop] = value
        return value

    def _get_max_overflow(self):
        """
        获取配置文件中max_overflow的值
        """
        prop = "pdbc.engine.max_overflow"
        value = self.__yaml_context.get_value(prop)
        prop = prop.split('.')[2]
        self.__engine_dict[prop] = value
        return value

    def _get_pool_recycle(self):
        """
        获取配置文件中pool_recycle的值
        """
        prop = "pdbc.engine.pool_recycle"
        value = self.__yaml_context.get_value(prop)
        prop = prop.split('.')[2]
        self.__engine_dict[prop] = value
        return value

    def _get_pool_timeout(self):
        """
        获取配置文件中pool_timeout的值
        """
        prop = "pdbc.engine.pool_timeout"
        value = self.__yaml_context.get_value(prop)
        prop = prop.split('.')[2]
        self.__engine_dict[prop] = value
        return value

    def _get_echo_pool(self):
        """
        获取配置文件中echo_pool的值
        """
        prop = "pdbc.engine.echo_pool"
        value = self.__yaml_context.get_value(prop)
        prop = prop.split('.')[2]
        self.__engine_dict[prop] = value
        return value

    def set_engine(self, **kwargs):
        """
        设置引擎

        你可以在调用PdbcTemplate内的方法之前，设置设置引擎需要的其他参数（不包括配置文件内的参数）

        :param kwargs: 除去配置文件中其他的值，采用key=value的形式
        :return: engine对象
        """
        self._logger: Logger
        url = self._get_url()

        if url is None:
            self._logger.error("yaml文件中的url为空")
        else:
            temp_dict = deepcopy(self.__engine_dict)
            temp_dict.pop("url")
            try:
                temp_list = []
                for key, value in temp_dict.items():
                    if value is None:
                        temp_list.append(key)
                for key in temp_list:
                    temp_dict.pop(key)
                if len(temp_dict) > 0:
                    self.__engine_dict.update(kwargs)
                    engine = create_engine(url, **temp_dict, **kwargs)
                else:
                    engine = create_engine(url)
                self._engine = engine
            except (SyntaxError, TypeError) as exc:
                self._logger.exception("通过函数传入的键值对，与yaml配置中的键值对，冲突", exc_info=exc)
            except ArgumentError as exc:
                self._logger.exception("无法解析yaml配置中的url", exc_info=exc)

    @property
    def engine(self) -> Engine:
        return self._engine

    @property
    def engine_dict(self):
        return self.__engine_dict

    def __new__(cls, *args, **kwargs):
        if cls.__pdbc_helper is None:
            cls.__pdbc_helper = object.__new__(cls)
        return cls.__pdbc_helper


class PdbcTemplate(PdbcOperations, PdbcHelper, SqlFormatter):
    """
    操作数据库的模板
    """

    @log
    def __init__(self):
        super().__init__()

    def execute(self, sql, *args, **kwargs):
        """
        使用sqlalchemy中的方法执行sql，建议sql类型为DDL(数据定义语言)时候使用

        如果sql为select，建议使用query方法

        如果sql为update，delete，insert，建议使用update方法

        :param sql: sql语句
        """
        with self.engine.connect() as con:
            return con.execute(sql, *args, **kwargs)

    def update(self, sql, *args):
        """
        更新数据库

        :param sql: sql语句
        :param args: 问号对应的值
        """
        sql = self._format(sql)
        key_list = []
        value_list = [*args]
        params = {}

        for i in range(97, 97 + len(args)):
            key_list.append(chr(i))

        index = 0
        for key in key_list:
            params[key] = value_list[index]
            index += 1

        with self.engine.connect() as con:
            con.execute(sa.text(sql), params)
            self._logger: Logger
            self._logger.info("更新数据成功")

    def query(self, sql, *args) -> Union[DataFrame, Iterator[DataFrame]]:
        """
        查询数据库

        :param sql: sql语句
        :param args: 问号对应的值
        :return: 数据
        """
        sql = self._format(sql)
        key_list = []
        value_list = [*args]
        params = {}

        for i in range(97, 97 + len(args)):
            key_list.append(chr(i))

        index = 0
        for key in key_list:
            params[key] = value_list[index]
            index += 1

        with self.engine.connect() as con:
            data = pd.read_sql(sa.text(sql), con, params=params)
            return data

    def query_table(self,
                    table_name,
                    schema=None,
                    index_col=None,
                    coerce_float=True,
                    parse_dates=None,
                    columns=None,
                    chunksize: Optional[int] = None) -> Union[DataFrame, Iterator[DataFrame]]:
        """
        使用pandas.read_sql_table方法，读取数据

        详情请看 https://pandas.pydata.org/docs/reference/api/pandas.read_sql_table.html#pandas.read_sql_table
        """
        with self.engine.connect() as con:
            return pd.read_sql_table(table_name,
                                     con,
                                     schema=schema,
                                     index_col=index_col,
                                     coerce_float=coerce_float,
                                     parse_dates=parse_dates,
                                     columns=columns,
                                     chunksize=chunksize
                                     )

    def update_table(self,
                     data: DataFrame,
                     name: str,
                     schema=None,
                     if_exists: str = "replace",
                     index: bool_t = False,
                     index_label=None,
                     chunksize=None,
                     dtype=None,
                     method=None):
        """
        使用pandas.to_sql方法，将数据写入数据库中的表中

        详情请看 https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_sql.html#pandas.DataFrame.to_sql
        """
        with self.engine.connect() as con:
            data.to_sql(name,
                        con=con,
                        schema=schema,
                        if_exists=if_exists,
                        index=index,
                        index_label=index_label,
                        chunksize=chunksize,
                        dtype=dtype,
                        method=method)

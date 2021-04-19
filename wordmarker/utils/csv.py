import pandas as pd


class CsvUtils(object):
    """
    ::

        csv文件工具类
    """

    @classmethod
    def read_csv(cls, file, skiprows=0, nrows=None, skipcols=0, ncols=None, encoding='utf-8'):
        """
        .. note::

            读取csv文件

        :param file: csv文件
        :param skiprows: 跳过的行数
        :param nrows: 要获取的行数
        :param skipcols: 跳过的列数
        :param ncols: 要获取的列数
        :param encoding: 编码方式
        :return: - 读取的结果
        """
        if nrows is not None and ncols is not None:
            usecols = cls.__generate_usecols(skipcols=skipcols, ncols=ncols)
            data = pd.read_csv(file, header=None, encoding=encoding, skiprows=skiprows, nrows=nrows,
                                 usecols=usecols)
        elif nrows is None and ncols is not None:
            usecols = cls.__generate_usecols(skipcols=skipcols, ncols=ncols)
            data = pd.read_csv(file, header=None, encoding=encoding, skiprows=skiprows, usecols=usecols)
        elif ncols is None and nrows is not None:
            usecols = cls.__generate_usecols(skipcols=skipcols, ncols=ncols)
            if len(usecols) > 0:
                data = pd.read_csv(file, header=None, encoding=encoding, skiprows=skiprows, nrows=nrows,
                                     usecols=lambda x: x not in usecols)
            else:
                data = pd.read_csv(file, header=None, encoding=encoding, skiprows=skiprows, nrows=nrows)
        else:
            usecols = cls.__generate_usecols(skipcols=skipcols, ncols=ncols)
            if len(usecols) > 0:
                data = pd.read_csv(file, header=None, encoding=encoding, skiprows=skiprows,
                                     usecols=lambda x: x not in usecols)
            else:
                data = pd.read_csv(file, header=None, encoding=encoding, skiprows=skiprows)
        return data

    @classmethod
    def __generate_usecols(cls, skipcols, ncols):
        usecols = []
        if ncols is not None:
            for i in range(skipcols, skipcols + ncols):
                usecols.append(i)
        else:
            for i in range(0, skipcols):
                usecols.append(i)
        return usecols

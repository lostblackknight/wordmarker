from abc import ABCMeta, abstractmethod


class Formatter(metaclass=ABCMeta):
    """
    格式化的抽象类
    """

    @abstractmethod
    def _format(self, *args):
        pass


class CsvFormatter(Formatter):
    def _format(self, data):
        pass


class SqlFormatter(Formatter):
    """
    格式化sql语句
    """

    def _format(self, sql):
        """
        格式化用户输入的sql

        例如：
            *输入*：     select * from t_user where username=? and password=?

            *格式化*：   select * from t_user where username=:a and password=:b

            *注意*：     拼接的 :a, :b 使用的是26个字母，也就是说一次查询的?，不能超过26个，超过26个后情况未知...
        :param sql: sql语句
        :return: 格式化后的sql语句
        """
        sql_list = list(sql)
        index = 0
        n = 97
        for i in sql_list:
            if i == '?':
                sql_list[index] = ':' + chr(n)
                n += 1
            index += 1
        return ''.join(sql_list)

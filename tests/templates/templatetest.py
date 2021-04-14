import unittest

from wordmarker.contexts import YamlContext, WordMarkerContext
from wordmarker.creatives import FactoryBean
from wordmarker.templates.csv_template import CsvHelper, CsvTemplate
from wordmarker.templates.pdbc_template import PdbcHelper, PdbcTemplate
import pandas as pd


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

    def test1(self):
        path = "E:\PycharmProjects\wordmarker\config.yaml"
        helper = PdbcHelper(path)
        print(helper.__engine_dict)
        engine = helper.set_engine()
        print(engine)
        print(helper.__engine_dict)
        print(type(engine))

    def test2(self):
        path = "E:\PycharmProjects\wordmarker\config.yaml"
        helper = PdbcHelper(path)
        template = PdbcTemplate(path)
        # template.execute("""
        # CREATE TABLE salgrade (
        #   grade int,
        #   losal int,
        #   hisal int(10)
        # )
        # """)
        # data = template.query('select * from t_user where id=? and username=?', 1, "张三")
        # res = template.query('select * from t_user where id=? and username=?', 1, "张三")
        # rs = template.update('insert into t_user values (?, ?, ?, ?)', 4, '展飞', '456', '2020-04-30')

        # print(rs)
        # print(res)

    def test3(self):
        path = "E:\PycharmProjects\wordmarker\config"
        YamlContext().path = path
        PdbcHelper()
        template = PdbcTemplate()
        # template.update('update t_user set username=? where id=?', '王三金', 1)
        data = template.query('select * from emp')
        print(data)
        # template.update_df(data, 't_name', index=False)

    def test4(self):
        path = "E:\PycharmProjects\wordmarker\config"
        YamlContext.instance(path)
        helper = CsvHelper()
        print(helper.get_csv_path())

    def test5(self):
        path = "E:\PycharmProjects\wordmarker\config"
        YamlContext.create_instance()
        helper = CsvHelper()
        print(CsvTemplate().get_csv_path())

    def test6(self):
        path = "E:\PycharmProjects\wordmarker\config"
        YamlContext.create_instance(path)
        helper = CsvHelper()
        print(helper.get_csv_path())

    def test7(self):
        f1 = FactoryBean()
        bean = f1.get_bean("factory_bean")
        print(id(bean))
        f2 = FactoryBean()
        bean2 = f2.get_bean("factory_bean")
        print(id(f2))
        print(id(bean2))
        print(f2.get_bean_names())

    def test8(self):
        context1 = WordMarkerContext("E:\PycharmProjects\wordmarker\config")

        template = CsvTemplate()
        print(template.get_csv())
        print(template.get_csv_file_name())
        # data = template.csv_to_df()
        # print(data['城市数据_加盐.csv'])
        p = PdbcTemplate()

        print(template.get_csv_out_path())

    def test9(self):
        context1 = WordMarkerContext("E:\PycharmProjects\wordmarker\config")
        template = CsvTemplate()
        data = template.csv_to_df()
        # print(data['城市数据_加盐.csv'])
        print(data['城市数据_加盐.csv'].to_csv("E:\PycharmProjects\wordmarker\data\out\oo.csv"))

    def test10(self):
        WordMarkerContext("E:\PycharmProjects\wordmarker\config")

        template = CsvTemplate()
        data_dict = template.csv_to_df()
        template.df_to_csv(data_dict)
        pt = PdbcTemplate()
        d = pt.query_table("t_user")
        template.df_to_csv({"user.csv": d})

    def test11(self):
        WordMarkerContext("")
        csv_template = CsvTemplate()
        data_dict = csv_template.csv_to_df()
        pdbc_template = PdbcTemplate()
        pdbc_template.update_table(data_dict['城市数据_加盐.csv'], "t_city_data")
        pdbc_template.update_table(data_dict['市场数据_加盐.csv'], "t_market_data")
        pdbc_template.update_table(data_dict['景气指数_加盐.csv'], "t_prosperity_index")


if __name__ == '__main__':
    unittest.main()

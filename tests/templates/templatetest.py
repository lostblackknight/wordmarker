import os
import unittest

from wordmarker.contexts import YamlContext, WordMarkerContext
from wordmarker.creatives import FactoryBean
from wordmarker.templates.csv_template import CsvHelper, CsvTemplate
from wordmarker.templates.word_template import DocxHelper, ImgHelper
from wordmarker.templates.pdbc_template import PdbcHelper, PdbcTemplate
import pandas as pd

from wordmarker.utils import PathUtils


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

    def test12(self):
        WordMarkerContext('E:\PycharmProjects\wordmarker-bake\config.yaml')
        helper = DocxHelper()
        print(helper.docx_in_path)
        print(helper.docx_out_path)
        print(helper.get_docx())
        print(helper.get_docx_file_name())

    def test13(self):
        WordMarkerContext('E:\PycharmProjects\wordmarker\config.yaml')
        p = PdbcTemplate()
        data = p.query(
            "select * from t_city_data, t_market_data where t_city_data.year_id=? or t_market_data.year_id=? limit 10 "
            "offset 0", 2016,
            2016)
        print(data)

    def test14(self):
        WordMarkerContext('E:\PycharmProjects\wordmarker\config.yaml')
        file_list = ['E:\\PycharmProjects\\wordmarker\\template\\in\\bbb.txt', 'b.doc', 'c.doc', 'd.doc', 'f.docx']
        suffix_list = ['.docx']
        print(PathUtils.filter_file(file_list, suffix_list))

    def test15(self):
        pass

    def test16(self):
        WordMarkerContext('E:\PycharmProjects\wordmarker\config.yaml')
        # print(DocxHelper().get_docx_in_path())
        h = DocxHelper()
        print(h.docx_in_path)
        i = ImgHelper()
        print(i.img_out_path)
        print(i.get_img_file("aaa.png"))


if __name__ == '__main__':
    unittest.main()

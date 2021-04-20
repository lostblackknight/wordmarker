import unittest

from wordmarker.contexts import YamlContext, WordMarkerContext
from wordmarker.creatives import FactoryBean
from wordmarker.loaders import DefaultResourceLoader
from wordmarker.templates import PdbcTemplate


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

    def test1(self):
        resource = DefaultResourceLoader().get_resource("E:\PycharmProjects\wordmarker\data\oo")
        # print(resources.get_file_name_prefix_suffix())
        # print(resources.get_file_name_prefix_suffix()['城市数据_加盐.csv'][1])
        print(resource.get_file())
        # print(resources.get_dir())
        # print(resources.get_file_name())

    def test2(self):
        pass

    def test3(self):
        loader = DefaultResourceLoader()
        resource = loader.get_resource("E:\PycharmProjects\wordmarker\data\城市数据_加盐.csv")
        data = loader.load(resource)
        print(data)

    def test4(self):
        res = DefaultResourceLoader().get_resource("f:/aa")
        print(res.get_file())

    def test5(self):
        yaml = YamlContext("E:\PycharmProjects\wordmarker\config")
        # print(yaml.get_yaml())
        print(yaml.get_value('username'))

    def test6(self):
        path = "E:\PycharmProjects\wordmarker\config.yaml"
        context = WordMarkerContext(path)
        yaml_context = context.yaml_context
        print(yaml_context.get_yaml())
        res = yaml_context.get_resource(yaml_context.path)
        print(res.get_file_encoding())
        print(res.get_file_name())

    def test7(self):
        path = "E:\PycharmProjects\wordmarker\config"
        context1 = WordMarkerContext(path)
        print(context1.yaml_context.get_value("data.csv.path"))
        print(context1.yaml_context.get_resource(path).get_file_encoding())
        print(id(context1))
        print(context1.bean_factory.get_bean_names())
        context2 = WordMarkerContext("E:\PycharmProjects\wordmarker\config\config.yaml")
        print(context2.yaml_context.get_value("data.csv.path"))
        print(id(context2))
        print(context2.bean_factory.get_bean_names())
        context3 = WordMarkerContext("E:\PycharmProjects\wordmarker\config\settings.yaml")
        print(context3.yaml_context.get_value("data.csv.path"))
        print(id(context3))
        print(context3.bean_factory.get_bean_names())

    def test8(self):
        context1 = WordMarkerContext("E:\PycharmProjects\wordmarker\config")
        t1 = PdbcTemplate()
        data = t1.query("select * from emp")
        print(data)
        print(context1.bean_factory.get_bean_names())
        context2 = WordMarkerContext("E:\PycharmProjects\wordmarker\config\config.yaml")
        t2 = PdbcTemplate()
        data = t2.query("select * from t_user")
        print(data)
        print(context2.bean_factory.get_bean_names())
        context3 = WordMarkerContext("E:\PycharmProjects\wordmarker\config\settings.yaml")
        t3 = PdbcTemplate()
        data = t3.query("select * from emp")
        print(data)
        print(context3.bean_factory.get_bean_names())

        data = t2.query("select * from emp")
        print(data)
        bb: FactoryBean = context2.bean_factory.get_bean("factory_bean")
        bb.add_bean("nihao", "你好")
        print(context2.bean_factory.get_bean_names())
        print(bb.get_bean("nihao"))

    def test9(self):
        context = WordMarkerContext("E:\\PycharmProjects\\wordmarker\\config\\config.yaml")
        yaml = context.yaml_context
        # print(yaml.get_value("data.csv.path"))
        # print(yaml.get_resource(yaml.path).get_file_encoding())
        # print(yaml.get_yaml())
        template = PdbcTemplate()
        # template.set_engine(hide_parameters=True)
        # print(template.engine.echo)
        data = template.update('update t_user set password=?, birthday=? where id=?', "133456", "2020-05-05", 5)

        # data = template.query("select * from t_user")
        # print(data)
        #
        # template.update_table(data, 't_test')
        # print(template.query_table('t_test'))



if __name__ == '__main__':
    unittest.main()

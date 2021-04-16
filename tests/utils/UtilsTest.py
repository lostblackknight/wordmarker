import unittest

from wordmarker.data.formatter import DocxFormatter
from wordmarker.utils import CsvUtils
from wordmarker.utils.file import PathUtils
from wordmarker.utils.yaml import YamlUtils


class MyTestCase(unittest.TestCase):
    def test_csvUtils(self, PathUtils=None):
        rp = PathUtils.get_root_path("wordmarker")
        reader = CsvUtils.read_csv(rp + "data/城市数据_加盐.csv", skipcols=1, skiprows=1, nrows=20)

        print(reader.iloc[:2])



    def test_pathUtils(self):
        util = PathUtils(r'E:\PycharmProjects\wordmarker\data\城市数据_加盐.csv', '../../d/c.txt')
        print(util.get_relative_path())

    def test_yamlUtils(self):
        res = YamlUtils.read_prop("number")
        print(type(res))
        print(res)


if __name__ == '__main__':
    unittest.main()

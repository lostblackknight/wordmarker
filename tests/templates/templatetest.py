import os
import unittest

from docx.shared import Mm
from docxtpl import InlineImage, R

from wordmarker.contexts import YamlContext, WordMarkerContext
from wordmarker.creatives import FactoryBean
from wordmarker.templates.csv_template import CsvHelper, CsvTemplate
from wordmarker.templates.word_template import DocxHelper, ImgHelper, TextHelper, WordTemplate
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
        print(helper._get_docx())
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

    def test17(self):
        WordMarkerContext('E:\PycharmProjects\wordmarker\config.yaml')
        h = TextHelper()
        print(h.text_in_path)
        # print(h.get_value("name"))
        print(h.get_yaml())
        print(h.get_yaml_singleton())
        print(h.get_yaml_singleton_str())

    def test18(self):
        WordMarkerContext('E:\PycharmProjects\wordmarker-bake\config.yaml')
        dh = DocxHelper()
        print(dh.docx_in_path)
        print(dh.docx_out_path)
        print(dh._get_docx()[0])
        print(dh.get_docx_file_name())

    def test19(self):
        WordMarkerContext('E:\PycharmProjects\wordmarker-bake\config.yaml')
        w = WordTemplate()
        # print(w.img_out_path)
        print(w.docx)
        print(w.docx_out_path)
        print(w.docx_in_path)
        print(w.text_in_path)
        print(w.img_out_path)
        f = open(w.img_out_path + w.path_separator + 'ccc.txt', mode='w')
        f.write('aaa')
        f.close()
        print(w.img_out_path)
        print(w.img_out_path)
        # print(w.get_img_file('aaa.png'))
        print(w.get_docx_file_name())
        print(w.path_separator)
        print(w.get_value('a.b.c'))
        # print(w.get_resource('__init__.py').get_file())
        # print(w.wt.tpl)
        # w.append({
        #     'aa': 'aa',
        #     'bb': 'bb'
        # }).append({
        #     'cc': 'cc',
        #     'dd': 'dd'
        # })
        # print(w.content)
        print(w.content)
        wt = WordTemplate()
        print(wt.img_out_path)
        print(wt.docx)
        print(wt.text_in_path)


    def test20(self):
        WordMarkerContext('E:\PycharmProjects\wordmarker-bake\config.yaml')
        wt = WordTemplate()
        context = {
            'page_break': R('\f'),
            'theme': '2017年航指数半年白皮书',
            'header': {
                'title': '导语：',
                'paragraphs': [
                    '转眼间2017年已过半，同时航指数也迎来了它的第三个夏天。一路走来航指数已经推出了四篇白皮书系列文章，虽然每篇由于时间和篇幅所限很多热点未能做到更详尽的深挖，但每次发布之后都会在业内引起不小的反响与关注，也因此给航指数带来了大量的“粉丝”。很多热心的朋友在看了白皮书后与我们取得了联系、进一步深入探讨民航市场动向，也为我们提出了诸多宝贵意见，在此我们要表示衷心的感谢。未来航指数会一直坚持最初的宗旨：“来源于行业、服务于行业”，并以开放的态度力争为行业提供更好的分析“干货”。',
                    '2017半年白皮书纵览上半年市场整体变化趋势，主要聚焦在国内、国际市场概况、旅客各类出行特征、节假日民航市场出行变化、国际出境热点分析等行业热点上。下半年展望中结合航指数网站相关数据，为分析判断提供科学有效的依据，对下半年的市场趋势及热点情况进行预判。',
                ],
                'author': '中国航信航指数团队',
                'date': '2017.7',
            },
            'main': [
                {
                    'h1': '上半年行业发展综述',
                    'h1_section': [
                        {
                            'h2': '1.全行业宏观概况——景气指数 显示民航市场整体运转良好，国内市场呈稳步上升态势；国际市场增速放缓，量价差距逐渐放缓；港澳台市场依旧在复苏之路上缓慢前行。',
                            'h2_section': [
                                {
                                    'h3': None,
                                    'h3_section': [
                                        {
                                            'img_title': '图1.景气指数',
                                            'img': InlineImage(wt.tpl, wt.get_img_file('景气指数.png'), width=Mm(160)),
                                            'explanation': [
                                                '2017年上半年民航全市场景气指数稳步上升：国内航线129，国际航线155，港澳台航线114。',
                                                '国内航线景气指数同比增幅为8%，增速超2016年同期4个百分点，市场稳步上升。',
                                                '国际航线景气指数增速放缓，同比增幅放缓至12%，但春节峰值周景气指数超越2016年峰值，达到178，再创新高。',
                                                '港澳台航线景气指数同比小幅下降1个百分点，市场依然在复苏道路上缓慢挣扎。',
                                            ],
                                        },
                                        {
                                            'img_title': '图2.量价指数',
                                            'img': InlineImage(wt.tpl, wt.get_img_file('量价指数.png'), width=Mm(160)),
                                            'explanation': [
                                                '2017年上半年民航市场运输量指数 整体上升；价格指数 在国内、国际航线市场趋于稳定，在港澳台航线市场有所上升。',
                                                '国内航线运输量指数179，同比增幅13%；价格指数93，同比增长3个百分点。',
                                                '国际航线量价差距逐渐放缓，运输量指数增速放缓，但上半年运输量指数依然突破250大关，以17%的同比增幅升至270；价格指数 则趋于稳定，同比持平。',
                                                '港澳台航线运输量指数148，同比下降6%；价格指数85，同比增幅8%，市场在复苏之路上缓慢前行。',
                                            ],
                                        },
                                        {
                                            'img_title': '图3.客座率指数',
                                            'img': InlineImage(wt.tpl, wt.get_img_file('客座率指数.png'), width=Mm(160)),
                                            'explanation': [
                                                '2017年上半年市场客座率 水平表现较为稳定，市场投放策略相对利好。',
                                                '国内航线客座率指数84%，国际航线客座率指数80%，均与2016年同期水平持平，产投比相对稳定。',
                                                '港澳台航线客座率指数77%，较2016年同期上涨1个百分点。',
                                            ],
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            'h2': '2.上半年民航旅客规模及特征',
                            'h2_section': [
                                {
                                    'h3': '国内市场：',
                                    'h3_section': [
                                        {
                                            'img_title': '图4.2017年上半年民航国内市场旅客概况',
                                            'img': InlineImage(wt.tpl, wt.get_img_file('2017年上半年民航国内市场旅客概况.png'), width=Mm(160)),
                                            'explanation': [
                                                '2017年上半年国内航线旅客规模 7857万，较2016年同期增长14%。但平均飞行距离由2016年同期的1246公里缩短到1237公里。（参见图4）',
                                                '国内航线人均重复购买率 2.66，较2016年同期的2.64上升0.02次。',
                                                '旅客规模扩增、人均重复购买率几乎保持平稳，民航市场旅客覆盖面或将逐渐扩大化。',
                                            ],
                                        },
                                        {
                                            'img_title': '图5.2017年上半年民航国内旅行者特征',
                                            'img': InlineImage(wt.tpl, wt.get_img_file('2017年上半年民航国内旅行者特征.png'), width=Mm(160)),
                                            'explanation': [
                                                '如图5所示，2017年上半年国内市场旅客性别比例基本与2016年同期保持稳定，男性旅客比例超女性7个百分点，依然占据市场主体优势。',
                                                '年龄分布方面有微小变化，24~30岁旅客出行比例同比下降1%，而60岁以上旅客出行比例同比上升1%，由航指数的节假日指数数据也可以看出60岁以上旅客在节假日出行比例上逐年上升，市场上层出不穷的“老年游”产品及充足的时间、良好的经济条件均促进了旅客的出游热情。',
                                                '上半年国内市场四成以上旅客提前预订天数 依然集中在航班起飞前3天内，但较2016年同期相比，提前1-3天预订的旅客比例下降1%，提前16-30天预订的旅客比例上升一个百分点。',
                                                '在国内市场中跟团出行市场比例较小，上半年仅有6%的旅客出行选择了跟团，较2016年同期下降1%；而在自由行旅客中超过半数为单独出行，1/4民航出行为双人结伴出行，两者较2016年同期均保持稳定。',
                                                '在值机环节虽然自助值机模式不断增加，柜台值机比例同比有4%的下降，但目前仍是旅客首选。提前3小时以内值机旅客比例同比下降3%，但仍占据七成以上的高位。',
                                            ],
                                        },
                                    ]
                                },
                                {
                                    'h3': '国际市场：',
                                    'h3_section': [
                                        {
                                            'img_title': '图6.2017年上半年民航国际市场旅客概况',
                                            'img': InlineImage(wt.tpl, wt.get_img_file('2017年上半年民航国际市场旅客概况.png'), width=Mm(160)),
                                            'explanation': [
                                                '2017年上半年民航国际航线旅客规模1667万人，同比增幅4%，增速低于国内市场10个百分点。平均飞行距离较2016年同期（2955公里）呈增长趋势，达到3243公里。（参见图6）',
                                                '国际航线旅客重复购买率1.93，继2016年上半年出现同比下降趋势后，2017年上半年同比呈现平稳状态，旅客出行习惯或将出现变动迹象。',
                                            ],
                                        },
                                        {
                                            'img_title': '图7.2017年上半年民航国际旅行者特征',
                                            'img': InlineImage(wt.tpl, wt.get_img_file('2017年上半年民航国际旅行者特征.png'), width=Mm(160)),
                                            'explanation': [
                                                '如图7所示，2017年上半年国际市场中以旅游为目的的民航旅客目的地偏好出现小范围变化，去往日韩朝的旅客除41~50年龄段比例有所上升外，其他年龄段同比降幅均在2%左右；各年龄段去往北美洲、东南亚及西南太平洋的旅客比例均有1%—4%不同程度的同比上升。',
                                                '国际市场的提前预订周期明显长于国内市场，47%的旅客提前一个月开始预订，较2016年同期上升3个百分点。',
                                                '国际出行旅客跟团比例明显高于国内，但近年来也呈现出下降趋势，上半年有1/4旅客选择跟团出游，较2016年同期下降8个百分点；而在自由行的旅客中独自出行的比例也略少于国内出行，近半数自由行旅客为两人以上结伴出行，与2016年同期保持稳定。',
                                            ],
                                        }
                                    ]
                                }
                            ]
                        },
                    ],
                },
                {
                    'h1': '上半年行业热点透视',
                    'h1_section': [
                        {
                            'h2': None,
                            'h2_section': [
                                {
                                    'h3': '节假日出行：三大类航线在节假日表现出很大差异化：国内航线保持相对稳定的增长态势；国际航线则增速明显放缓；港澳台市场则在复苏之路上缓慢前行。',
                                    'h3_section': [
                                        {
                                            'img_title': '图8.2017年上半年节假日市场概况',
                                            'img': InlineImage(wt.tpl, wt.get_img_file('2017年上半年节假日市场概况.png'), width=Mm(160)),
                                            'explanation': [
                                                '如图8所示，2017年春节长假依然是日均旅客量最多的假期，国内航线增长加快，同比增幅达到16%，超2016年同期13个百分点；除春节外的其他小长假，国内航线同样保持着相对稳定的增长态势。',
                                                '国际航线则出现明显的增速放缓态势，元旦、春节、五一小长假的日均旅客量同比增幅已放缓至10%以下，甚至在清明、端午小长假出现了负增长现象。',
                                                '港澳台航线在上半年前四个小长假表现欠佳，持续呈负增长趋势，且春节小长假的日均旅客量已下降至13%；然而在端午小长假中港澳台市场日均旅客量表现出利好的复苏迹象，同比上升7个百分点，但未来市场发展如何还需进一步观察。',
                                            ],
                                        }
                                    ]
                                },
                                {
                                    'h3': '“萨德”致中—韩航线失利：由于“萨德”事件影响，2017年3月3日，国家旅游局在官网发布《赴韩国旅游提示》后国内多家旅游企业全面下架韩国游产品。随后一周中，中-韩航线未来一个月航班预订量出现了大量的取消。',
                                    'h3_section': [
                                        {
                                            'img_title': '图9.赴韩旅客量增长走势',
                                            'img': InlineImage(wt.tpl, wt.get_img_file('赴韩旅客量增长走势.png'), width=Mm(160)),
                                            'explanation': [
                                                '如图9所示，2015年MERS疫情使得赴韩旅客量断崖式下跌，以致2016年6-8月的旅客量呈爆发式增长，之后从9月开始，赴韩旅客量增长走势逐渐回归常态。',
                                                '2017年初随着“萨德”事件的推进及民众的强烈抗议，3月初中—韩航线再次迎来市场“寒冬”，赴韩旅客取消量倍增，3-6月赴韩旅客量同比下降45%。',
                                                '鉴于多种因素的影响，3月后中-韩航线各月运力投放同样出现了不同程度的缩减，3-6月运力投放同比下降36%。',
                                            ],
                                        }
                                    ]
                                },
                                {
                                    'h3': '中-澳旅游年助力民航市场：2017年为中-澳旅游年，宽松的对华签证政策为民航市场带来了新动力。多家航司加大运力投放力度，迎来旅客量高涨的同时客座率也明显上升。',
                                    'h3_section': [
                                        {
                                            'img_title': '图10.中澳间执飞航线图',
                                            'img': InlineImage(wt.tpl, wt.get_img_file('中澳间执飞航线图.png'), width=Mm(160)),
                                            'explanation': [
                                                '2017年上半年共有7家国内航空公司运营中-澳航线，分别是国航、东航、南航、海航、厦航、川航和首都航空，其中涉及航线28条。',
                                                '执飞的28条航线中，国航、东航、南航三大航共占据六成以上的市场份额。开通中—澳航线的城市中广州是最多的也是唯一一个拥有5条不同航线的城市。',
                                            ],
                                        },
                                        {
                                            'img_title': '图11.上半年赴澳旅客量增长走势',
                                            'img': InlineImage(wt.tpl, wt.get_img_file('上半年赴澳旅客量增长走势.png'), width=Mm(160)),
                                            'explanation': [
                                                '如图11所示，自2016年中澳关系逐渐升温，旅客赴澳热情高涨，很大程度上推动了中-澳航线的运力投放力度，2017年1-6月月度运力增幅均超过25%。',
                                                '宽松利好的签证政策及大量的运力投放同时也一并带来了良好的市场反馈，2017年上半年赴澳旅客量平均同比增幅达到了27%。产投匹配度相一致，市场投放策略相对利好。',
                                            ],
                                        },
                                        {
                                            'img_title': '图12.2017上半年赴澳目的地分布情况',
                                            'img': InlineImage(wt.tpl, wt.get_img_file('2017上半年赴澳目的地分布情况.png'), width=Mm(160)),
                                            'explanation': [
                                                '如图12所示，2017上半年赴澳目的地中旅客量前5的澳大利亚城市依次为悉尼、墨尔本、布里斯班、珀斯和阿德莱德，其中去往悉尼和墨尔本的旅客量占到了市场总额的87%。',
                                                '2016年年底新开航线涉及的阿德莱德虽市场份额较少，但2017年上半年旅客量市场份额已接近老航线珀斯，市场潜力不可小觑。',
                                                '布里斯班毗邻黄金海岸市，近年来火热的海岛游需求也间接带动了布里斯班旅客量的逐年上涨，2017年上半年旅客量增长气势十足，同比增幅34%，已超过第一、二大城市的增长水平。',
                                            ],
                                        }
                                    ]
                                }
                            ]
                        },
                    ]
                },
                {
                    'h1': '下半年市场展望与预测',
                    'h1_section': [
                        {
                            'h2': '1.市场趋势预测',
                            'h2_section': [
                                {
                                    'h3': '指数预测',
                                    'h3_section': [
                                        {
                                            'img_title': '图13.景气指数预测走势图',
                                            'img': InlineImage(wt.tpl, wt.get_img_file('景气指数预测走势图.png'), width=Mm(160)),
                                            'explanation': [
                                                '国内航线暑运峰值期或将拉长，峰值区间相对平滑，整个暑运期间景气指数将维持在134以上；十一假期国内航线景气指数有望迎来5个百分点增长。',
                                                '国际航线下半年将又一次刷新峰值，景气指数将在8月初迎来峰值期，较2016年同期增幅有望达到14%。',
                                                '港澳台市场在下半年的两个波峰期尖点景气指数均有望达到120以上峰值，且在波谷期表现优于去年，淡季低点较去年略有提升。'
                                            ],
                                        },
                                        {
                                            'img_title': '图14.量价指数值预测走势图',
                                            'img': InlineImage(wt.tpl, wt.get_img_file('量价指数值预测走势图.png'), width=Mm(160)),
                                            'explanation': [
                                                '预计2017下半年市场运输量指数将维持在高位，国内航线运输量指数有望保持在180以上，国际航线运输量指数或将突破300到达350的新高度，港澳台航线运输量指数平稳维持在150—180之间。',
                                                '价格指数方面，国内航线价格指数十一假期之前尚能维持在90以上，假期过后则逐渐降至80左右。',
                                                '国际航线价格指数则整体低于国内航线，暑期过半价格指数开始逐渐走低，十一假期过后将在70以下浮动。'
                                            ],
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            'h2': '2.下半年热点展望',
                            'h2_section': [
                                {
                                    'h3': '暑运前瞻',
                                    'h3_section': [
                                        {
                                            'img_title': '图15.2017年暑运市场概况展望',
                                            'img': InlineImage(wt.tpl, wt.get_img_file('2017年暑运市场概况展望.png'), width=Mm(160)),
                                            'explanation': [
                                                '如图15所示，国内航线运力投放稳定增长，同比2016年暑期增投20%。截止到六月底的预订量增幅暂（17%）低于运力投放增幅，但就2016年同期来说，预订量市场表现仍处于稳步上升趋势。',
                                                '国际航线较2016年增速相比出现增长乏力现象，运力投放同比2016年暑期增投6%。但其预订量却较2016年同期下降了3个百分点，供大于求的市场状态使得今年暑期的国际市场充满了悬念。',
                                                '港澳台航线暑期市场就目前展望而言表现欠佳，无论从运力投放或同期的预订水平都低于2016年同期。'
                                            ],
                                        },
                                        {
                                            'img_title': '图16.2017年暑运国内重点市场',
                                            'img': InlineImage(wt.tpl, wt.get_img_file('2017年暑运国内重点市场.png'), width=Mm(160)),
                                            'explanation': [
                                                '如图16所示，国内市场暑期重点投放城市依然是上半年的热点城市，TOP10重点城市依次为北京、上海、广州、重庆、西安、成都、昆明、深圳、杭州、郑州。',
                                                '重点市场的暑期预订量除北京与昆明之外，其他城市均高于2016年同期，西安与郑州的预订增幅均优于国内航线整体水平，市场基础与增长潜力并存。',
                                                '重点市场今年投放座位量增幅最大的城市为重庆，增幅达到46%，而预订量增幅最大的城市为新晋十强的郑州，增幅可达40%。'
                                            ],
                                        },
                                        {
                                            'img_title': '图17.2017年暑运出入境重点航线',
                                            'img': InlineImage(wt.tpl, wt.get_img_file('2017年暑运出入境重点航线.png'), width=Mm(160)),
                                            'explanation': [
                                                '如图17所示，2017年暑运出入境市场的运力投放排名中，越南同比增幅最高48%，预订量增长也遥遥领先其他航线，达到83%；“中澳旅游年”的开幕推动了中—澳航线运力投放新增长，同比增幅达46%。',
                                                '中—韩航线市场“寒冬”依旧持续，暑运期间运力投放同比下降42%，预订量同比下降64%。中-日及中-泰航线分别位列出入境航线运力投放的第一、二位，然而其运力投放增幅和预订量增幅有明显放缓趋势，甚至出现了负增长情况，市场需求将逐渐趋于稳定。',
                                                '港澳台市场方面，中国内地往返香港和台湾的航线无论从运力投放还是同期预订量均出现不同幅度下滑；中国内地-澳门航线运力投放略好于港台市场，但预订量也有小幅下滑。'
                                            ],
                                        }
                                    ]
                                },
                                {
                                    'h3': '十一黄金周展望',
                                    'h3_section': [
                                        {
                                            'img_title': '图18.2017年十一黄金周出入境热点',
                                            'img': InlineImage(wt.tpl, wt.get_img_file('2017年十一黄金周出入境热点.png'), width=Mm(160)),
                                            'explanation': [
                                                '如图18所示，展望2017年十一黄金周旅客预订偏好，东南亚区域为当前最大的出入境热点，占据预订市场份额24%；日韩朝较去年同期相比失去了8%的市场份额。',
                                                '往返北美洲、港澳台和欧洲区域的预订需求份额相近；港澳台所占份额低于去年同期，市场需求动力不足。',
                                                '基于出入境整体市场的迅速扩张，中-美航线持续火热的市场需求仅使北美区域预订份额增长1个百分点；中东、西南太平洋区域要想抢占更多国际市场份额仍需更有吸引力的元素激发市场潜力。'
                                            ],
                                        },
                                    ]
                                }
                            ]
                        }
                    ]
                }
            ],
            'footer': {
                'title': '结语：',
                'paragraphs': [
                    '随着“一带一路”的提出与推进，打造世界级城市群和机场群成为崛起经济全球化时代的显著特征，同时也给航空运输业的发展带来了新的机遇和新的挑战。随着城市群和机场群的发展，航空运输市场多样化趋势愈加明显，航空服务不断向价值链两端延伸，这也给民航业管理理念、经营模式以及政府监管方式带来了巨大挑战。在这样的发展过程中，能为政府机构、航空公司、机场以及处于民航产业链上各行各业，以精准的数据结合科学的研判方法，及时的洞悉市场变幻风云，提供更加直接高效的决策支撑，将是航指数不懈努力的方向。',
                ],
                'annotation': {
                    'title': '注释：',
                    'content': [
                        '[注1]景气指数：是一种综合性指标，综合考虑市场运输量规模、价格水平和行业投入产出比计算得到，以2011年100点作为基准。',
                        '[注2]运输量指数：反应行业市场规模变化，以客公里指标为基础的计算指标，以2011年100点作为基准。',
                        '[注3]价格指数：反应旅客支付价格变化，以客公里收益为基础的计算指标，以2011年100点作为基准。',
                        '[注4]客座率：反应行业的投入产出比指标，客座率=客公里/座公里',
                        '[注5]旅客规模：按旅客个体计算，通过证件唯一识别和确定民航旅客，多次乘坐飞机的旅客记为1个个体。',
                        '[注6]重复购买率：每个旅客购买机票的平均次数。',
                        '[注7]提前预订天数：旅客起飞日期与旅客PNR创建日期之差。',
                        '[注8]暑运：7月1日至8月31日。'
                    ]
                }
            },
        }
        wt.append(context)
        wt.build('2017年航指数半年白皮书—发布版（新）.docx')


if __name__ == '__main__':
    unittest.main()

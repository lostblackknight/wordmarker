from wordmarker.contexts import WordMarkerContext
from wordmarker.templates import CsvTemplate, PdbcTemplate


def build_data_base():
    """
    构建数据库环境脚本
    """
    WordMarkerContext("config.yaml")
    csv_template = CsvTemplate()
    data_dict = csv_template.csv_to_df()
    pdbc_template = PdbcTemplate()
    pdbc_template.update_table(data_dict['城市数据_加盐.csv'], "t_city_data")
    pdbc_template.update_table(data_dict['市场数据_加盐.csv'], "t_market_data")
    pdbc_template.update_table(data_dict['景气指数_加盐.csv'], "t_prosperity_index")

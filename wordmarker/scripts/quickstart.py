import os
import shutil
import click
from ruamel.yaml import YAML

path_separator = os.path.sep

inp_standard = """
# ======================================================================================================

# ----------------------配置数据库信息
#
# 详细信息请查看 https://docs.sqlalchemy.org/en/14/core/engines.html
# url:
#    postgresql: "postgresql://username:password@localhost:5432/database"
#    mysql: mysql+pymysql://username:password@localhost:3306/database
# echo: 是否开启日志
# encoding: 编码，默认utf-8
# pool_size: 连接池大小
# max_overflow: 连接的数量，以允许在连接池"溢出"
# pool_recycle: 在给定的秒数过去之后，此设置将导致池回收连接。默认为-1。例如，设置为3600表示一小时后将回收连接
# pool_timeout: 放弃从池中获得连接之前要等待的秒数
# echo_pool: 是否开启日志
pdbc:
  engine:
    url: {url}
    echo: false
    encoding: utf-8
    pool_size: 5
    max_overflow: 10
    pool_recycle: -1
    pool_timeout: 30.0
    echo_pool: false

# ======================================================================================================

# ----------------------配置csv文件信息
#
# path: 文件的输入路径，可以是文件，也可以是目录
#       路径分隔符为 '/' 或 '\\'
#       path的值为相对于当前yaml文件的路径
# dir: 文件的输出目录
#      路径分隔符为 '/' 或 '\\'
#      dir的值为相对于当前yaml文件的路径
data:
  csv:
    input:
      path: data/in
    output:
      dir: data/out
  docx:
    input:
      path: template/in
    output:
      dir: template/out
  img:
    output:
      dir: img
  text:
    input:
      path: text

# ======================================================================================================
"""

inp_custom = """
# ======================================================================================================

# ----------------------配置数据库信息
#
# 详细信息请查看 https://docs.sqlalchemy.org/en/14/core/engines.html
# url:
#    postgresql: "postgresql://username:password@localhost:5432/database"
#    mysql: mysql+pymysql://username:password@localhost:3306/database
# echo: 是否开启日志
# encoding: 编码，默认utf-8
# pool_size: 连接池大小
# max_overflow: 连接的数量，以允许在连接池"溢出"
# pool_recycle: 在给定的秒数过去之后，此设置将导致池回收连接。默认为-1。例如，设置为3600表示一小时后将回收连接
# pool_timeout: 放弃从池中获得连接之前要等待的秒数
# echo_pool: 是否开启日志
pdbc:
  engine:
    url: {url}
    echo: false
    encoding: utf-8
    pool_size: 5
    max_overflow: 10
    pool_recycle: -1
    pool_timeout: 30.0
    echo_pool: false

# ======================================================================================================

# ----------------------配置csv文件信息
#
# path: 文件的输入路径，可以是文件，也可以是目录
#       路径分隔符为 '/' 或 '\\'
#       path的值为相对于当前yaml文件的路径
# dir: 文件的输出目录
#      路径分隔符为 '/' 或 '\\'
#      dir的值为相对于当前yaml文件的路径
data:
  csv:
    input:
      path: ''
    output:
      dir: ''
  docx:
    input:
      path: ''
    output:
      dir: ''
  img:
    output:
      dir: ''
  text:
    input:
      path: ''

# ======================================================================================================
"""


def generate_yaml(url, flag):
    yaml = YAML()
    if flag:
        content = yaml.load(inp_standard.format(url=url))
    else:
        content = yaml.load(inp_custom.format(url=url))
    current_dir = os.path.abspath(os.curdir)
    with open(current_dir + path_separator + "config.yaml", encoding='utf-8', mode='w') as f:
        yaml.dump(content, f)


@click.command()
def main():
    click.echo()
    click.echo("欢迎使用 WordMarker 的脚手架，请按照提示完成项目的构建。")
    url = database()
    flag = input_output()
    generate_yaml(url, flag)
    click.echo()
    end()


def database():
    dialect = database_dialect()
    return database_config(dialect)


def database_dialect():
    click.echo("-------------------------------------------------")
    click.echo("配置数据库")
    click.echo("-------------------------------------------------")
    click.echo("1. PostgreSQL")
    click.echo("2. MySql")
    click.echo("3. Oracle")
    click.echo("4. Microsoft")
    return click.prompt("数据库的类型，默认为", type=click.IntRange(1, 4), default=1)


def database_config(dialect):
    if dialect == 1:
        username = database_username("postgres")
        password = database_password()
        host = database_host("localhost")
        port = database_port(5432)
        name = database_name()
        return database_url(dialect, username, password, host, port, name)
    elif dialect == 2:
        username = database_username("root")
        password = database_password()
        host = database_host("localhost")
        port = database_port(3306)
        name = database_name()
        return database_url(dialect, username, password, host, port, name)
    elif dialect == 3:
        username = database_username("")
        password = database_password()
        host = database_host("localhost")
        port = database_port(1521)
        name = database_name()
        return database_url(dialect, username, password, host, port, name)
    elif dialect == 4:
        username = database_username("")
        password = database_password()
        host = database_host("localhost")
        port = database_port(1433)
        name = database_name()
        return database_url(dialect, username, password, host, port, name)


def database_username(username):
    return click.prompt("用户名，默认为", type=str, default=username)


def database_password():
    return click.prompt("密码，默认为", type=str, default="123456")


def database_host(host):
    return click.prompt("主机，默认为", type=str, default=host)


def database_port(port):
    return click.prompt("端口，默认为", type=int, default=port)


def database_name():
    return click.prompt("要连接的数据库", type=str)


def database_url(dialect, username, password, host, port, name):
    if dialect == 1:
        return f"postgresql://{username}:{password}@{host}:{port}/{name}"
    elif dialect == 2:
        return f"mysql+pymysql://{username}:{password}@{host}:{port}/{name}"
    elif dialect == 3:
        return f"oracle://{username}:{password}@{host}:{port}/{name}"
    elif dialect == 4:
        return f"mssql+pymssql://{username}:{password}@{host}:{port}/{name}"


def input_output():
    click.echo("-------------------------------------------------")
    click.echo("配置输入输出目录")
    click.echo("-------------------------------------------------")
    if click.confirm("是否启用默认的目录配置，默认为 [Y]", default=True):
        current_dir = os.path.abspath(os.curdir)
        if os.path.exists(current_dir + path_separator + "data"):
            shutil.rmtree(current_dir + path_separator + "data")
        if os.path.exists(current_dir + path_separator + "template"):
            shutil.rmtree(current_dir + path_separator + "template")
        if os.path.exists(current_dir + path_separator + "img"):
            shutil.rmtree(current_dir + path_separator + "img")
        if os.path.exists(current_dir + path_separator + "text"):
            shutil.rmtree(current_dir + path_separator + "text")
        os.makedirs(current_dir + path_separator + "data" + path_separator + "in")
        click.echo("成功创建data/in目录")
        os.makedirs(current_dir + path_separator + "data" + path_separator + "out")
        click.echo("成功创建data/out目录")
        os.makedirs(current_dir + path_separator + "template" + path_separator + "in")
        click.echo("成功创建template/in目录")
        os.makedirs(current_dir + path_separator + "template" + path_separator + "out")
        click.echo("成功创建template/out目录")
        os.makedirs(current_dir + path_separator + "img")
        click.echo("成功创建img目录")
        os.makedirs(current_dir + path_separator + "text")
        click.echo("成功创建text目录")
        return True
    else:
        current_dir = os.path.abspath(os.curdir)
        if os.path.exists(current_dir + path_separator + "data"):
            shutil.rmtree(current_dir + path_separator + "data")
        if os.path.exists(current_dir + path_separator + "template"):
            shutil.rmtree(current_dir + path_separator + "template")
        if os.path.exists(current_dir + path_separator + "img"):
            shutil.rmtree(current_dir + path_separator + "img")
        if os.path.exists(current_dir + path_separator + "text"):
            shutil.rmtree(current_dir + path_separator + "text")
        return False


def end():
    click.echo("成功构建项目 ^_^ !")


if __name__ == '__main__':
    main()

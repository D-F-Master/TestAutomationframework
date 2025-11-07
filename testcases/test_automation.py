import pymysql
import requests
import pytest

from utils import http_client
from utils.read_excel import read_excel
from jsonpath_ng import parse

# 自动执行test_data
class Test_Automation:
    # 调用read_excel()读取data文件空间下的表格
    data = read_excel()

    # 创建全局变量all
    all = {}

    # 数据驱动装饰器
    @pytest.mark.parametrize('case', data)
    def test_automation(self,case):

        # 引入全局变量
        all = self.all

        # 提取每行的数据发起请求
        method = case['method']
        url = http_client.base_url + case['path']
        headers = eval(case['headers']) if isinstance(case['headers'], str)else None  #三元运算府  条件成立执行 if 条件 else 条件不成立执行
        params = eval(case['params']) if isinstance(case['params'], str)else None
        data = eval(case["data"]) if isinstance(case["data"], str) else None
        json = eval(case["json"]) if isinstance(case["json"], str) else None
        files = eval(case["files"]) if isinstance(case["files"], str) else None

        # 创建请求数据字典
        request_data = {
            "method": method,
            "url": url,
            "headers": headers,
            "params": params,
            "data": data,
            "json": json,
            "files": files
        }

        # 发起请求
        response = requests.request(**request_data)  #..request_data 解包操作 把字典解包为请求


        # 如果case["check"]存在，表格中check字段为json表达式
        if case["check"]:
            # 判断json表达式的值是否等于预期
            assert parse(case["check"]).find(response.json())[0].value == case["expected"]
        else:
            # 判断预期是否存在与返回值中
            assert case["expected"] in response.json()

        # 数据库断言，对表格中的数据库请求进行断言判断。sql_check为sql语句，sql_expected为预期值
        if case['sql_check'] and case['sql_expected']:
            # 数据库连接配置
            config = {
                'host': http_client.host,
                'port': int(http_client.port),  # 确保端口为整数类型
                'user': http_client.user,
                'password': http_client.password,
                'database': http_client.database,
                'charset': http_client.charset
            }

            connection = None  # 初始化变量
            cursor = None  # 初始化变量

            try:
                # 建立连接
                connection = pymysql.connect(**config)
                # 创建存在光标
                cursor = connection.cursor()
                # 光标执行查询
                cursor.execute(case['sql_check'])
                # 返回结果
                result = cursor.fetchone()
                # 对结果进行断言
                assert result[0] == case['sql_expected']

            except Exception as e:
                print("数据库操作出错:", e)

            finally:
                # 关闭连接
                if cursor:
                    cursor.close()
                if connection:
                    connection.close()



        # json提取 例:{"TOKEN":"$..token"} 通过value的json表达式，从请求结果中提取数据通过键值对的方法存入全局变量all中
        if case['jsonExData']:
            # 将jsonExData转变为字典,进行遍历
            for key,value in eval(case['jsonExData']).items():
                value = parse(value).find(response.json())[0].value
                all[key] = value
                pass



        # SQL提取，格式{"id":"select id from employee where username = 'admin'"}
        if case['sqlExData']:
            for key, value in eval(case['sqlExData']).items():

                # 数据库连接配置
                config = {
                    'host': http_client.host,
                    'port': int(http_client.port),  # 确保端口为整数类型
                    'user': http_client.user,
                    'password': http_client.password,
                    'database': http_client.database,
                    'charset': http_client.charset
                }

                connection = None  # 初始化变量
                cursor = None  # 初始化变量

                try:
                    # 建立连接
                    connection = pymysql.connect(**config)
                    # 创建存在光标
                    cursor = connection.cursor()
                    # 光标执行查询
                    cursor.execute(value)
                    # 返回结果
                    result = cursor.fetchone()
                    # 写入全局变量
                    all[key]= result[0]

                except Exception as e:
                    print("数据库操作出错:", e)

                finally:
                    # 关闭连接
                    if cursor:
                        cursor.close()
                    if connection:
                        connection.close()



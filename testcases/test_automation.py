import logging

import pytest
from jinja2 import Template

from utils.allure_utils import allure_init
from utils.analyse_case_utils import analyse_case
from utils.asserts_utils import http_assert, sql_assert
from utils.extracto_utils import json_extracto, sql_extracto
from utils.read_excel import read_excel

from utils.requests_utils import send_http_request


# 自动执行test_data
class Test_Automation:
    # 调用read_excel()读取data文件空间下的表格
    data = read_excel()

    # 创建全局变量all
    all = {}

    # 数据驱动装饰器
    @pytest.mark.parametrize('case', data)
    def test_automation(self, case):
        # 引入全局变量
        all = self.all

        # 应用全局变量，使用jinja2进行渲染
        case = eval(Template(str(case)).render(all))

        # 初始化allure
        allure_init(case=case)

        # 记录日志
        logging.info(f"0.用例ID:{case['id']} 模块:{case['feature']} 场景:{case['story']} 标题:{case['title']}")

        # 解析case并创建请求数据字典
        request_data = analyse_case(case)

        # 发起请求
        response = send_http_request(request_data)

        # 对http请求进行断言
        http_assert(case, response)

        # 对sql请求进行断言
        sql_assert(case)

        # json提取
        json_extracto(case, response, all)

        # SQL提取
        sql_extracto(case, all)

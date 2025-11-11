import logging

import allure
from jsonpath_ng import parse

from utils.requests_utils import send_sql_request


@allure.step("3.对http请求进行断言")
def http_assert(case, response):
    # 如果case["check"]存在，表格中check字段为json表达式
    if case["check"]:
        # 判断json表达式的值是否等于预期
        logging.info(f"3.对数据:{case["check"]}是否等于预期{case["expected"]}进行断言")
        assert parse(case["check"]).find(response.json())[0].value == case["expected"]
    else:
        # 判断预期是否存在与返回值中
        logging.info(f"3.对预期:{case["expected"]}是否存在与{response.json()}进行断言")
        assert case["expected"] in response.json(), f'预期与结果不符'


def sql_assert(case):
    # 数据库断言，对表格中的数据库请求进行断言判断。sql_check为sql语句，sql_expected为预期值
    if case['sql_check'] and case['sql_expected']:
        sql_assert_execute(case)

# 为了避免没有调用sql断言的用例，在报告中显示在请求前先进行判断
@allure.step("3.对sql请求进行断言")
def sql_assert_execute(case):
    logging.info(f"3.对预期:{case['sql_check']}是否存在与{case['sql_expected']}进行断言")
    response = send_sql_request(case['sql_check'])
    assert response == case['sql_expected']
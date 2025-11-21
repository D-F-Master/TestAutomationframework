import logging

import allure
from jsonpath_ng import parse

from utils.requests_utils import send_sql_request


@allure.step("对http请求的返回值进行断言")
def http_assert(case, response):
    expected = eval(case['expected'])
    # 如果case["check"]存在，表格中check字段为json表达式
    if case["check"]:
        check = eval(case['check'])
        for check, expected in zip(check,expected):
            # 判断json表达式的值是否等于预期
            logging.info(f"http响应断言内容 实际结果: {case["check"]} == 预期结果: {case["expected"]} ")
            assert parse(check).find(response.json())[0].value == expected
    else:
        for e in expected:
            # 判断预期是否存在与返回值中
            logging.info(f"http响应断言内容 预期结果: {case["check"]} == 实际结果: {response.json()}")
            assert e in response.json(), f'预期与结果不符'

def sql_assert(case):
    # 数据库断言，对表格中的数据库请求进行断言判断。sql_check为sql语句，sql_expected为预期值
    if case['sql_check'] and case['sql_expected']:
        sql_assert_execute(case)


# 为了避免没有调用sql断言的用例，在报告中显示在请求前先进行判断
@allure.step("对sql请求进行断言")
def sql_assert_execute(case):
    response = send_sql_request(case['sql_check'])
    logging.info(f"对sql请求的返回值断言sql_expected: {case['sql_expected']} ")

    assert response == case['sql_expected']

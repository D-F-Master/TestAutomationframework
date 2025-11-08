import logging

import allure
from jsonpath_ng import parse

from utils.requests_utils import send_sql_request


# json提取 例:{"TOKEN":"$..token"} 通过value的json表达式，从请求结果中提取数据通过键值对的方法存入全局变量all中
def json_extracto(case, response, all):
    if case['jsonExData']:
        json_extracto_execute(case, response, all)


# SQL提取，格式{"id":"select id from employee where username = 'admin'"}
def sql_extracto(case, all):
    if case['sqlExData']:
        sql_extracto_execute(case, all)

@allure.step('4.JSON提取')
def json_extracto_execute(case, response, all):
    # 将jsonExData转变为字典,进行遍历
    for key, value in eval(case['jsonExData']).items():
        value = parse(value).find(response.json())[0].value
        all[key] = value
    logging.info(f"4.JSON提取,根据{case['jsonExData']}提取，此时的全局变量ALL为{all}")


@allure.step('4.SQL提取')
def sql_extracto_execute(case, all):
    for key, value in eval(case['sqlExData']).items():
        all[key] = send_sql_request(value)
    logging.info(f"4.SQL提取，根据{case['sqlExData']}提取，此时的全局变量ALL为{all}")
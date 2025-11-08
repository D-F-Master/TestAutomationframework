import logging

from config.config import *

import allure

@allure.step("1.请求数据解析")
def analyse_case(case):

    # 提取每行的数据发起请求
    method = case['method']
    url = BASE_URL + case['path']
    headers = eval(case['headers']) if isinstance(case['headers'], str) else None  # 三元运算府  条件成立执行 if 条件 else 条件不成立执行
    params = eval(case['params']) if isinstance(case['params'], str) else None
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

    logging.info(f"1.请求数据解析:{request_data}")
    allure.attach(f"{request_data}", name = '数据解析结果')
    return request_data
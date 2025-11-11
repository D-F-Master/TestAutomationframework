import logging

from config.config import *
from utils.ocr_utils import dddd_ocr_text

import allure

@allure.step("1.请求数据解析")
def analyse_case(case):

    # 提取每行的数据发起请求
    method = case['method'].strip()
    url = BASE_URL + case['path'].strip()
    headers = eval(case['headers'].strip()) if isinstance(case['headers'], str) else None  # 三元运算府  条件成立执行 if 条件 else 条件不成立执行
    params = eval(case['params'].strip()) if isinstance(case['params'], str) else None
    data = eval(case["data"].strip()) if isinstance(case["data"], str) else None
    json = eval(case["json"].strip()) if isinstance(case["json"], str) else None
    files = eval(case["files"].strip()) if isinstance(case["files"], str) else None

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

    # 日志
    logging.info(f"用例数据:{request_data}")

    allure.attach(f"{request_data}", name = '用例数据')

    return request_data
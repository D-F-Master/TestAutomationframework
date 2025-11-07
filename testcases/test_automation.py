import requests
import pytest

from utils import http_client
from utils.read_excel import read_excel
from jsonpath_ng import parse

class Test_Automation:
    data = read_excel()

    all = {}

    @pytest.mark.parametrize('case', data)
    def test_automation(self,case):
        # 提取数据
        method = case['method']
        url = http_client.base_url + case['path']
        # 三元运算，如果是字符串就转换为字典，否则为空
        headers = eval(case['headers']) if isinstance(case['headers'], str)else None
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

        # 解包请求数据
        response = requests.request(**request_data)

        # assert response.json()['code'] == case['expected']
        # 如果check字段不为空，就判断实际校验字段与预期结构，否则就判断预期结构是否包含在实际结果中
        # 如果check字段不为空，表示需要使用JSONPath进行精确字段校验
        if case["check"]:
            # 使用jsonpath_ng的parse函数解析check字段中的JSONPath表达式
            # 并在响应JSON数据中查找匹配的字段
            matches = parse(case["check"]).find(response.json())

            # 如果找到了匹配的字段
            if matches:
                # 断言第一个匹配项的值等于预期值
                assert matches[0].value == case["expected"]
            else:
                # 如果没有找到匹配项，则抛出断言错误
                raise AssertionError(f"JSONPath '{case['check']}' not found in response")
        else:
            # 如果check字段为空，则使用简单的包含性检查
            # 断言预期值包含在响应JSON中
            assert case["expected"] in response.json()


        # 数据库断言，对数据库的内容进行断言判断
        if case['sql_check'] and case['sql_expected']:


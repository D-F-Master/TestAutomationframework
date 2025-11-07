import pytest
import requests

from utils import http_client
from utils.read_excel import read_excel


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

        assert response.json()['code'] == case['expected']



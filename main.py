import os
import pytest

from utils import http_client

if __name__ == '__main__':
    # 将所有参数放在一个列表中
    pytest.main([
        # 设置pytest-rerunfailures模块的参数
        f'--reruns={http_client.reruns}',
        f'--reruns-delay={http_client.reruns_delay}'
    ])

    # 调用allure生成报告
    os.system("allure generate -o report -c temps")

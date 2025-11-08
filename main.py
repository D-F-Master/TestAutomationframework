import os
import pytest

from utils import config_utils

if __name__ == '__main__':
    pytest.main([
        # 设置pytest-rerunfailures模块的参数
        f'--reruns={config_utils.reruns}',
        f'--reruns-delay={config_utils.reruns_delay}'
    ])

    # 调用allure生成报告
    os.system("allure generate -o report -c temps")


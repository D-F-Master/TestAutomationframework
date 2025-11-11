import os
import pytest

from config.config import *

if __name__ == '__main__':
    pytest.main([
        # 设置pytest-rerunfailures模块的参数
        f'--reruns={RERUNS}',
        f'--reruns-delay={RERUNS_DELAY}'
    ])

    # 调用allure生成报告
    os.system("allure generate -o report -c temps")


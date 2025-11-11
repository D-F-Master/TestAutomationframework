import logging

import allure


def allure_init(case):
    # 初始化allure
    allure.dynamic.feature(case['feature'])
    allure.dynamic.story(case['story'])
    allure.dynamic.title(f'ID:{case["id"]} -- {case["title"]}')
    # 日志
    logging.info(f"Allure - feature(模块) : {case['feature']}, story(场景) : {case['story']}, title(标题) : {case['id']}--{case['title']}")

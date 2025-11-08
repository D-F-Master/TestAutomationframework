import allure


def allure_init(case):
    # 初始化allure
    allure.dynamic.feature(case['feature'])
    allure.dynamic.story(case['story'])
    allure.dynamic.title(f'ID:{case["id"]} -- {case["title"]}')
import logging

import allure
import pymysql
import requests

from config.config import *


@allure.step("发送http请求")
def send_http_request(request_data):
    response = requests.request(**request_data)
    allure.attach(f"{response.json()}", name='http请求返回结果')
    logging.info(f"http请求的返回值{response.json()}")
    return response  # ..request_data 解包操作 把字典解包为请求



@allure.step("发送sql请求")
def send_sql_request(sql, index=0):
    logging.info(f"发送sql请求: {sql}")
    # 数据库连接配置
    config = {
        'host': HOST,
        'port': int(PORT),  # 确保端口为整数类型
        'user': USER,
        'password': PASSWORD,
        'database': DATABASE,
        'charset': CHARSET
    }

    connection = None  # 初始化变量
    cursor = None  # 初始化变量

    try:
        # 建立连接
        connection = pymysql.connect(**config)
        # 创建存在光标
        cursor = connection.cursor()
        # 光标执行查询
        cursor.execute(sql)
        # 获取查询结果
        result = cursor.fetchone()
         # 返回指定索引的结果
        response = result[index]
        # 注意：这里不应该对基本数据类型调用 json() 方法
        allure.attach(f"{response}", name='sql请求返回结果')
        logging.info(f'sql请求的返回值: {response}')
        return response


    except Exception as e:
        logging.error(f"数据库操作出错: {e}")
        return None

    finally:
        # 关闭连接
        if cursor:
            cursor.close()
        if connection:
            connection.close()


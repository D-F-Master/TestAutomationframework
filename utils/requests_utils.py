import logging

import allure
import pymysql
import requests

from config.config import *


@allure.step("2.发送http请求")
def send_http_request(request_data):
    logging.info(f"2.发送http请求:{request_data}")
    return requests.request(**request_data)  # ..request_data 解包操作 把字典解包为请求


def send_sql_request(sql, index=0):
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
        # 返回结果
        return cursor.fetchone()[index]


    except Exception as e:
        print("数据库操作出错:", e)

    finally:
        # 关闭连接
        if cursor:
            cursor.close()
        if connection:
            connection.close()

# 测试自动化框架

## 使用方法

1. 执行`pip install-r requirements.txt`下载依赖包
2. 执行`python main.py`启动测试

执行main.py文件即可，若是需要修改用例，在data文件夹下的test_data添加上用例即可。

## 配置说明

所有配置的修改都在config中修改

```
application:
  #  测试服务器基础地址
  base_url: "http://192.168.31.10:8080"
  #  重试次数
  reruns : 2
  #  次数间隔时间
  reruns-delay : 1


#数据库配置
database:
  # 数据库主机地址
  host: "localhost"
  # 数据库端口号
  port: "3306"
  # 数据库用户名
  user: "root"
  # 数据库密码
  password: "2002"
  # 数据库名
  database: 'green_mall_batabase'
  # 编码
  charset: 'utf8mb4'
```

## test_data字段说明



## utils工具类说明



## 项目根目录 

├── data                  # 用于保存 Excel 格式的测试用例 

├── testcases             # 用于保存 test_runner.py 

├── utils                 # 用于保存各种工具类/函数，例如读取 Excel 文件的工具函数 

├── pytest.ini            # 配置日志等 pytest 相关设置 

├── run.py                # 运行入口脚本 

├── log                   # 用于保存运行日志 

├── report                # 用于生成测试报告（如 Allure 报告）

├── file                  # 涉及文件上传接口时，用于存放上传的文件 

├── config                # 用于保存配置信息，如 BASE_URL、数据库连接信息等 

└── conftest.py           # 存放全局钩子函数，用于测试用例执行前后的数据初始化和销毁




# 基础URL配置
BASE_URL = "http://localhost:8080"

# http://localhost:8080/admin/plant/GetPlantAllList
# http://192.168.10.141/api/cloud-api

# 测试重试配置
RERUNS = 1
RERUNS_DELAY = 1

# 数据库配置
HOST = "localhost"  # 数据库主机地址
PORT = "3306"       # 数据库端口号
USER = "root"       # 数据库用户名
PASSWORD = "2002"   # 数据库密码
DATABASE = 'green_mall_batabase'  # 数据库名
CHARSET = 'utf8mb4' # 编码格式

TEST_DATA_FILE_PATH = './data/test_data.xlsx'
TEST_DATA_SHEET_NAME = 'Sheet1'

# 飞书机器人地址
webhook = 'https://open.feishu.cn/open-apis/bot/v2/hook/0dafa074-8380-4afb-91d2-1b869ce1033c'

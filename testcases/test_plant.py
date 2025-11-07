import pytest
from utils import http_client
from utils.logger import get_logger

# 获取logger实例
logger = get_logger(__name__)


@pytest.fixture(scope='session')
def token():
    logger.info("开始获取登录token...")
    response = http_client.post('/admin/employee/login', json={'username':'admin','password':'123456'})
    token = response.json()['data']['token']
    logger.info("成功获取登录token")
    yield token


def test_get_plant_category(token):
    logger.info("开始测试获取植物分类")
    response = http_client.get('/admin/plant/plantCategory', token=token).json()
    logger.info(f"获取到的植物分类数据: {response['data']}")
    assert '水培植物' in response['data'][0]['description'], "期望在返回数据中找到'水培植物'"
    logger.info("测试通过: 成功找到'水培植物'分类")
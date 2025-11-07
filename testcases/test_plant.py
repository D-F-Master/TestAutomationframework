import pytest
from utils import http_client

@pytest.fixture(scope='session')
def token():
    response = http_client.post('/admin/employee/login', json={'username':'admin','password':'123456'})
    token = response.json()['data']['token']
    yield  token


def test_get_plant_category(token):
    response = http_client.get('/admin/plant/plantCategory',token = token).json()
    assert '水培植物' in response['data'][0]['description']
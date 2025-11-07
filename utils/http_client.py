import requests
import yaml
import os

# 模块级变量，只加载一次
_current_dir = os.path.dirname(os.path.abspath(__file__))
_config_path = os.path.join(_current_dir, '..', 'config', 'config.yml')

with open(_config_path, 'r', encoding='utf-8') as config:
    _data = yaml.safe_load(config)

base_url = _data['application']['base_url']


def get(url, token = None, params=None):
    return requests.get(base_url + url, params=params, headers={'token': token})


def post(url, token = None, json=None):
    return requests.post(base_url + url, json=json, headers={'token': token})

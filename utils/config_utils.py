import yaml
import os

# 模块级变量，只加载一次
_current_dir = os.path.dirname(os.path.abspath(__file__))
_config_path = os.path.join(_current_dir, '..', 'config', 'config.yml')

with open(_config_path, 'r', encoding='utf-8') as config:
    _data = yaml.safe_load(config)

base_url = _data['application']['base_url']
reruns = _data['application']['reruns']
reruns_delay = _data['application']['reruns-delay']

host = _data['database']['host']
# 数据库端口号
port =  _data['database']['port']
# 数据库用户名
user =  _data['database']['user']
# 数据库密码
password = _data['database']['password']
# 数据库名
database = _data['database']['database']
# 编码
charset =  _data['database']['charset']

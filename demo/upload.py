import requests
from jsonpath_ng import parse
if __name__ == '__main__':
    response = requests.post('http://192.168.31.10:8080/admin/employee/login',json={
        'username':'admin',
        'password':'123456'
    })

    data = response.json()

    token = parse('$..token').find(data)[0].value



    upload_data = {
        'method': 'post',
        'url': 'http://192.168.31.10:8080/admin/common/localUpload',
        'files': None,
        'headers': {
            'token':token
        }
    }

    upload_data['files'] = {
        'file1':('1.png', open('../file/img.png', 'rb'), 'png')
    }

    requests.request(**upload_data)
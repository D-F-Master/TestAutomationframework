import requests
from config.config import webhook

def send_allura_url():
    message_data = {
        "msg_type": "post",
        "content": {
            "post": {
                "zh_cn": {
                    "title": "测试报告生成完毕",
                    "content": [
                        [{
                            "tag": "text",
                            "text": "allura报告生成完成"
                        }, {
                            "tag": "a",
                            "text": "请查看",
                            "href": 'http://localhost:63342/TestAutomationframework/report/index.html?_ijt=r67rmhoktv7j59di5tk59d2988&_ij_reload=RELOAD_ON_SAVE'
                        }
                        ]
                    ]
                }
            }
        }
    }
    return requests.post(webhook, json=message_data)


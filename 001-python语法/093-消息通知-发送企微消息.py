import sys

import requests
import json


def send_text_to_wechat(text, key):
    """
    发送文本消息到企业微信机器人
    :param text: str 要发送的文本
    :param key: str 机器人 Webhook 地址中的 key
    :return: str 发送结果
    """
    # 拼接机器人 Webhook 地址
    webhook_url = f"https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={key}"

    # 要发送的消息内容
    message = {
        "msgtype": "text",
        "text": {
            "content": text
        }
    }

    # 发送 POST 请求
    response = requests.post(webhook_url, data=json.dumps(message))

    # 返回发送结果
    return response.content.decode("utf-8")


if __name__ == '__main__':
    # key = "c8f3582d-0d44-4185-b296-a2742500ceca"
    # text = "Hello World!"
    key = sys.argv[0]
    text = str(sys.argv[0])
    result = send_text_to_wechat(text, key)
    print(result)

import requests
from retrying import retry

counts = 0
@retry(wait_fixed=1000, stop_max_attempt_number=3)
def send_request():
    global counts
    counts += 1
    print("第{}次请求".format(counts))
    # 发送请求
    response = requests.get("https://www.example.com",  timeout=0.01)

    # 请求成功，则返回响应对象
    return response

print(send_request())
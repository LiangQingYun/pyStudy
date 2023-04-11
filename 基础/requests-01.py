# # 写一个requests案例，用于请求一个网页
# import requests
#
# # 发起一个请求
# search = input('请输入搜索内容：')
# print(search)
# url = f'https://www.sogou.com/web?query={search}'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.41'
# }
# response = requests.get(url, headers)
# # 获取响应数据
# response.encoding = 'utf-8'
# page_text = response.text
# print(page_text)
# # 获取响应码
# print(response.status_code)
#
# response.close()
import difflib

similarity = difflib.SequenceMatcher(None, "为什么说斜疝是定时炸弹？", "为什么说伤胃则伤肺？.mp4").ratio()
print(similarity)


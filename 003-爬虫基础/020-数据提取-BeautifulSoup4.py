from bs4 import BeautifulSoup

"""
    BS4 解析HTML文档(会解析整个文档  速度会相对较慢)
"""

"""
html.parser是Python自带的HTML解析器，速度较慢，容错能力较强
lxml：基于libxml2的高性能HTML解析器，速度较快，可用XPath进行解析和搜索。
html5lib：可以解析HTML5的解析器，速度较慢，但能够处理各种奇怪的HTML代码。
"""

with open('../002-前端基础/002-Html常见标签.html', encoding='UTF-8') as file:
    html = file.read()

soup = BeautifulSoup(html, 'lxml')
print(soup.prettify())  # 格式化输出

# 选择第一个p标签
soup.find('p')

# 选择所有p标签
soup.find_all('p')

# 选择class属性为“example”的标签
soup.find_all(class_='example')

# 选择id属性为“content”的标签
soup.find_all(id='content')
# 类选择器
li_tags = soup.select('.item')
# id选择器
div = soup.select_one('#content')

# 获取 ul 对象
ul = soup.find('ul')

# 遍历获取 ul 对象下的 li 标签
for li in ul.find_all('li'):
  print(li.string)

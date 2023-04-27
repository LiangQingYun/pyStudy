from lxml import html

# 读取本地 HTML 文件
with open('../002-前端基础/002-Html常见标签.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 使用 lxml 库解析 HTML 内容
tree = html.fromstring(content)

# 使用 XPath 表达式提取标题元素
titles = tree.xpath('//h1/text()')

# 打印标题元素
print(titles)

# 写一个xpath案例，解析html中的数据
# 1. 导入lxml库
from lxml import etree

# 2. 读取html文件
html = etree.parse("test.html")

# 3. 获取所有的li标签
li_list = html.xpath("//li")
print(li_list)

# 4. 获取所有li标签中class的属性值
li_list = html.xpath("//li/@class")
print(li_list)

# 5. 获取所有li标签中class的属性值为item-0的li标签
li_list = html.xpath("//li[@class='item-0']")
print(li_list)

# 6. 获取所有li标签中class的属性值为item-0的li标签下的a标签的href属性值
li_list = html.xpath("//li[@class='item-0']/a/@href")
print(li_list)

# 7. 获取所有li标签中class的属性值为item-0的li标签下的a标签的文本值
li_list = html.xpath("//li[@class='item-0']/a/text()")
print(li_list)

# 8. 获取所有li标签中class的属性值为item-0的li标签下的a标签的文本值
li_list = html.xpath("//li[@class='item-0']/a")
print(li_list[0].xpath("./text()"))
print(li_list[0].xpath("./@href"))

# 9. 获取所有li标签中class的属性值为item-0的li标签下的a标签的文本值
li_list = html.xpath("//li[@class='item-0']/a")
print(li_list[0].xpath("text()"))
print(li_list[0].xpath("@href"))

# 10. 获取所有li标签中class的属性值为item-0的li标签下的a标签的文本值
li_list = html.xpath("//li[@class='item-0']/a")
print(li_list[0].xpath("string(.)"))
print(li_list[0].xpath("@href"))

# 11. 获取所有li标签中class的属性值为item-0的li标签下的a标签的文本值
li_list = html.xpath("//li[@class='item-0']/a")


# 写一个下载视频的案例



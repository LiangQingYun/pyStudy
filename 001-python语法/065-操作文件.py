"""
    r：只读模式（默认）
    w：写入模式（会覆盖已有的文件内容）
    a：追加模式（不会覆盖已有的文件内容）
    x：创建新文件并写入（如果文件已经存在，会报错）
    b：以二进制模式打开文件
    t：以文本模式打开文件（默认）
"""
# 打开文件，并使用 with 语句
with open('test.txt', 'w') as file:
    # 向文件中写入内容
    file.write('Hello, world!\n')

# 打开文件，并使用 with 语句
with open('test.txt', 'r') as file:
    # 读取文件内容，并输出到控制台
    content = file.read()
    print(content)

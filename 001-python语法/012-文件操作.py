"""
    r：只读模式，默认模式，如果文件不存在会抛出异常；
    w：写模式，如果文件存在会覆盖原有内容，如果文件不存在会创建新文件；
    x：独占写模式，如果文件已存在会抛出异常，用于避免意外覆盖文件；
    a：追加模式，用于在文件末尾追加内容，如果文件不存在会创建新文件；
    b：二进制模式，与其它模式搭配使用，用于处理二进制文件；
    t：文本模式，与其它模式搭配使用，用于处理文本文件，是默认模式。
"""
# 打开文件
file = open('example.txt', 'w')

# 写入数据
file.write('Hello, World!\n')
file.write('This is an example file.\n')

# 关闭文件
file.close()

# 读取文件
file = open('example.txt', 'r')

# 读取整个文件
content = file.read()
print(content)

# 关闭文件
file.close()

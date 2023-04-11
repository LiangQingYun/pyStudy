import socket

# 服务器地址
# 本地测试,先启动服务端 , 再启动客户端
HOST = 'localhost'
PORT = 12345

# 注意协议类型要一致
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.connect((HOST, PORT))  # 连接服务器

    while True:
        message = input('请输入你要发送的消息: ')  # 从控制台读入消息
        s.sendall(message.encode())  # 将消息发送给服务器 (字符串转为字节类型)
        data = s.recv(1024)  # 接收服务器返回的消息，最多接收 1024 字节数据
        print('Received', repr(data.decode()))  # 输出服务器返回的消息


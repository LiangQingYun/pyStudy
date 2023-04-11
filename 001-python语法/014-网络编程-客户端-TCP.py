"""
TCP 先建立连接 , 后通信 , 再断开连接
    1. 创建套接字
    2. 建立连接 -- 三次握手  四次挥手
    3. 发送数据
    4. 关闭套接字

与UDP 的区别:
    1. TCP 是面向连接的 , UDP 是无连接的
    2. TCP 提供可靠的服务 , UDP 不保证可靠交付
    3. UDP没有明显的区分客户端和服务端 , TCP 需要建立连接
    4. TCP 传输数据量大 , UDP 传输数据量小


"""

import socket

# 定义主机地址和端口号
HOST = 'localhost'
PORT = 12345

# 创建 TCP Socket 对象
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接服务器
client_socket.connect((HOST, PORT))

# 发送数据
message = 'Hello, server!'
client_socket.sendall(message.encode())

# 接收数据
data = client_socket.recv(1024)
print('收到服务端消息:', data.decode())

# 关闭套接字
client_socket.close()

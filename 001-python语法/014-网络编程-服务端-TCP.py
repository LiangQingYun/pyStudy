import socket

# 定义主机地址和端口号
HOST = 'localhost'
PORT = 12345

# 创建 TCP Socket 对象
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定主机地址和端口号
server_socket.bind((HOST, PORT))

# 监听客户端连接 , 参数指定最大连接数
server_socket.listen(1)

print('等待客户端连接...')

# 循环接受客户端连接请求
while True:
    # 等待客户端连接   返回值是一个元组 , 元组的第一个元素是客户端套接字 , 第二个元素是客户端地址
    client_socket, client_address = server_socket.accept()

    print(f'客户端 {client_address} 已连接')

    try:
        # 接收客户端数据
        data = client_socket.recv(1024)
        print(f'收到客户端消息: {data.decode()}')

        # 发送响应数据
        response = 'Hello, client!'
        client_socket.sendall(response.encode())

    except Exception as e:
        print('通信异常:', e)

    finally:
        # 关闭客户端套接字
        client_socket.close()

# 关闭服务器套接字
server_socket.close()

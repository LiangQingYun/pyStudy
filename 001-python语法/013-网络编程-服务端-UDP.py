import socket

"""
端口范围  0-65535   2^16
ip表示的是一个32位的二进制数，每8位用十进制表示一位，共4位，用点分隔开
ip表示机器的地址   端口表示机器上的一个进程(分配给应用)
端口一般使用1024以上的端口 , 0-1023的端口是系统保留的端口 

socket 实现不同主机之间进程间的通信
"""

"""
    创建一个TCP/IP套接字
    socket.AF_INET  表示网络类型 = IPv4    还有IPv6 
    socket.SOCK_STREAM 表示协议类型 = TCP协议  还有UDP协议
    UDP(无连接) 
        速度快
        结构简单
        但是 - 不安全, 可能丢包
        在网络直播 , 游戏 , 视频会议等领域使用
    TCP(有连接)
        速度慢
        结构复杂
        但是 - 安全, 不会丢包
"""
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定到本地地址和端口
server_address = ('localhost', 12345)
server_socket.bind(server_address)

while True:
    # 接收客户端消息和地址
    print('等待客户端消息...')
    data, client_address = server_socket.recvfrom(1024)
    print(f'收到来自{client_address}的消息：{data.decode()}')

    # 发送确认消息给客户端
    message = '已收到消息'
    server_socket.sendto(message.encode(), client_address)

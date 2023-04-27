import socket

def is_valid_ip(ip_address):
    try:
        socket.inet_aton(ip_address)
        return True
    except socket.error:
        return False

ip_address = "192.168.0.1"
if is_valid_ip(ip_address):
    print("Valid IP address")
else:
    print("Invalid IP address")
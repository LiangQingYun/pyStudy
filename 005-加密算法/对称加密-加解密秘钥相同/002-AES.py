from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import binascii

def encrypt_AES(data, key, iv):
    # 创建AES加密器对象，使用CBC模式和提供的偏移量（IV）
    cipher = AES.new(key.encode("utf-8"), AES.MODE_CBC, iv.encode("utf-8"))

    # 对数据进行填充并加密
    ct_bytes = cipher.encrypt(pad(data.encode("utf-8"), AES.block_size))

    # 将加密后的字节数据转换为十六进制字符串
    return binascii.hexlify(ct_bytes).decode("utf-8")

def decrypt_AES(encrypted, key, iv):
    # 创建AES解密器对象，使用CBC模式和提供的偏移量（IV）
    cipher = AES.new(key.encode("utf-8"), AES.MODE_CBC, iv.encode("utf-8"))

    # 将十六进制字符串转换为字节数据
    ct_bytes = binascii.unhexlify(encrypted)

    # 解密数据并去除填充
    decrypted = unpad(cipher.decrypt(ct_bytes), AES.block_size)

    # 将解密后的字节数据转换为字符串
    return decrypted.decode("utf-8")

if __name__ == '__main__':
    # 该密钥的二进制长度为 32 * 4 = 128 位
    key = "c8a63a564412888d83adaeddeb1304BF"
    # 该偏移量的二进制长度为 16 * 4 = 64 位
    iv = "lianou0000000000"
    data = "Hello, AES!"

    # 加密
    encrypted = encrypt_AES(data, key, iv)
    print("Encrypted (Hex):", encrypted)

    # 解密
    decrypted = decrypt_AES(encrypted, key, iv)
    print("Decrypted:", decrypted)

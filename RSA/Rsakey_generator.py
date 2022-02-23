#RSA 私钥公钥生成器（1024），1024对应最大加密数据长度为117字节，超长数据需拆分或增加密钥长度

from Crypto import Random
from Crypto.PublicKey import RSA

random_generator = Random.new().read
rsa = RSA.generate(1024, random_generator)
# 生成私钥
private_key = rsa.exportKey()
print(private_key.decode('utf-8'))
# 生成公钥
public_key = rsa.publickey().exportKey()
print(public_key.decode('utf-8'))

with open('rsa_private_key.pem', 'wb')as f:
    f.write(private_key)

with open('rsa_public_key.pem', 'wb')as f:
    f.write(public_key)

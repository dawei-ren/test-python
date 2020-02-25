"""
rsa 非对称加密 解密
"""

import rsa


def new_keys():
    f, e = rsa.newkeys(2048)  # 生成公钥、私钥
    e = e.save_pkcs1()  # 保存为 .pem 格式
    with open("e.pem", "wb") as x:  # 保存私钥
        x.write(e)
    f = f.save_pkcs1()  # 保存为 .pem 格式
    with open("f.pem", "wb") as x:  # 保存公钥
        x.write(f)


def a():
    y = b"abcdefg1234567"

    # 加密
    with open("f.pem", "rb") as x:
      f = x.read()
      f = rsa.PublicKey.load_pkcs1(f) # load 公钥，由于之前生成的私钥缺少'RSA'字段，故无法 load
    cipher_text = rsa.encrypt(y, f) # 使用公钥加密
    print(cipher_text)

    # 解密
    with open("e.pem", "rb") as x:
      e = x.read()
      e = rsa.PrivateKey.load_pkcs1(e)  # load 私钥
    text = rsa.decrypt(cipher_text, e)  # 使用私钥解密
    # assert text == y  # 断言验证
    # sign = rsa.sign(y, e, "SHA-256") # 使用私钥进行'sha256'签名
    # verify = rsa.verify(y, sign, f) # 使用公钥验证签名
    # print(verify)
    print(text)


if __name__ == '__main__':
    # new_keys()
    a()
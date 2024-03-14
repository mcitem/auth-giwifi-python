from Crypto.Cipher import AES
import base64
def zero_pad(data, block_size=AES.block_size):
    pad_length = block_size - (len(data) % block_size)
    return data + bytes([0] * pad_length)
def cryptoEncode(oriData,iv):
    oriData = oriData.encode('utf-8')
    iv = iv.encode('utf-8')
    key=b'1234567887654321'
    aes =AES.new(key,AES.MODE_CBC,iv)
    padData = zero_pad(oriData)
    encrypted = aes.encrypt(padData)
    cryptoData = base64.b64encode(encrypted)
    return cryptoData.decode('utf-8')
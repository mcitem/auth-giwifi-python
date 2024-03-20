from Crypto.Cipher import AES
import base64
def cryptoEncode(oriData,iv):
    oriData = oriData.encode('utf-8')
    key=b'1234567887654321'
    aes =AES.new(key,AES.MODE_CBC,iv.encode('utf-8'))
    oriData+=bytes([0]*(AES.block_size-(len(oriData)%AES.block_size)))
    encrypted = aes.encrypt(oriData)
    cryptoData = base64.b64encode(encrypted)
    return cryptoData.decode('utf-8')
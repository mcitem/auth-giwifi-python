from Crypto.Cipher import AES
from bs4 import BeautifulSoup
import requests,random,json,base64,sys
def cryptoEncode(oriData,iv):
    oriData = oriData.encode('utf-8')
    key=b'1234567887654321'
    aes =AES.new(key,AES.MODE_CBC,iv.encode('utf-8'))
    oriData+=bytes([0]*(AES.block_size-(len(oriData)%AES.block_size)))
    encrypted = aes.encrypt(oriData)
    cryptoData = base64.b64encode(encrypted)
    return cryptoData.decode('utf-8')
# config
IP='192.168.99.120'
username=sys.argv[1]
password=sys.argv[2]
if len(sys.argv)>3:
    baseIP=sys.argv[3]

headers = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.5.1.4 Safari/537.36"}
a=[]
for i in BeautifulSoup(requests.get(f'http://{IP}/gportal/web/login',headers=headers).text, 'html.parser').find(id="frmLogin").find_all(['input'], type=['text', 'hidden','password']):
    n,v = i.get('name'),i.get('value')
    if n:
        if n=="name":
            v+=username
        elif n=="password":
            v+=password
        elif n=="userMac":
            v=" "
        elif n=="iv":
            iv=v
        elif n=="sign":
            sign=v
        a.append(f"{n}={v}")
print(str(json.loads(requests.post(f'http://{IP}/gportal/web/authLogin?round='+str(random.randint(0, 999)),headers=headers,data={'data':cryptoEncode("&".join(a),iv),'iv':iv}).text)))
print(str(json.loads(requests.post(f'http://{IP}/gportal/web/queryAuthState',headers=headers).text)))
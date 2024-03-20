import requests,random,json
from bs4 import BeautifulSoup
from cryptoEncode import cryptoEncode

# config
username=''
password=''
baseIP='192.168.99.120'


baseURL='http://'+baseIP
headers = {
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.5.1.4 Safari/537.36"
}

html = requests.get(baseURL+'/gportal/web/login',headers=headers).text

soup = BeautifulSoup(html, 'html.parser')
frmLogin = soup.find(id="frmLogin")
arr = []
for i in frmLogin.find_all(['input'], type=['text', 'hidden','password']):
    name = i.get('name')
    value = i.get('value')
    if name:
        if name=="name":
            value+=username
        elif name=="password":
            value+=password
        elif name=="userMac":
            value=" "
        elif name=="iv":
            iv=value
        elif name=="sign":
            sign=value
        arr.append(f"{name}={value}")
oriData = "&".join(arr)
cryptoData=cryptoEncode(oriData,iv)

res=requests.post(baseURL+'/gportal/web/authLogin?round='+str(random.randint(0, 999)),headers=headers,data={'data':cryptoData,'iv':iv})
res1=requests.post(baseURL+'/gportal/web/queryAuthState',headers=headers)
print(str(json.loads(res.text)))
print(str(json.loads(res1.text)))
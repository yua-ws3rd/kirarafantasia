import uuid
from  requesthash import *
from str import *
import requests
import collections
import string
import random
import urllib3

urllib3.disable_warnings()  # 方便抓包

def getname():
    seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=-"
    sa = []
    for i in range(8):
        sa.append(random.choice(seed))
    salt = ''.join(sa)
    return salt
def signup():
    api1 = 'player/signup'
    uuidr = str(uuid.uuid1())#uuid也是登录凭证之一。。。
    payload = '{"uuid":"'+uuidr+'","platform":2,"name":"'+getname()+'","stepCode":1}'
    header = collections.OrderedDict(
        [('Unity-User-Agent', 'app/0.0.0; Android OS 7.1.1 / API-25 NMF26F/7.11.16; Xiaomi MI MIX 2'),
         ('X-STAR-REQUESTHASH', getrequesthash(api1, sessionID=None, json1=payload)),
         ('X-Unity-Version', '5.5.4f1'),
         ('X-STAR-AB', X_STAR_AB),
         ('Content-Type', 'application/json; charset=UTF-8'),
         ('User-Agent', 'Dalvik/2.1.0 (Linux; U; Android 7.1.1; MI MAX 2 MIUI/7.11.16)'),
         ('Host', 'krr-prd.star-api.com'),
         ('Connection', 'Keep-Alive'),
         ('Accept-Encoding', 'gzip')])
    req = requests.post(api_host+api1,data=payload,headers = header,verify = False).json()
    return [0,req['playerId'],req['accessToken'],uuidr]

def login(accessToken,uuidt):
    api2 = 'player/login'
    payload = '{"uuid":"'+uuidt+'","accessToken":"'+accessToken+'","platform":2,"appVersion":"1.0.3"}'
    header = collections.OrderedDict(
        [('Unity-User-Agent', 'app/0.0.0; Android OS 7.1.1 / API-25 NMF26F/7.11.16; Xiaomi MI MIX 2'),
         ('X-STAR-REQUESTHASH', getrequesthash(api2, sessionID=None, json1=payload)),
         ('X-Unity-Version', '5.5.4f1'),
         ('X-STAR-AB', X_STAR_AB),
         ('Content-Type', 'application/json; charset=UTF-8'),
         ('User-Agent', 'Dalvik/2.1.0 (Linux; U; Android 7.1.1; MI MAX 2 MIUI/7.11.16)'),
         ('Host', 'krr-prd.star-api.com'),
         ('Connection', 'Keep-Alive'),
         ('Accept-Encoding', 'gzip')])
    req = requests.post(api_host+api2,data=payload,headers = header,verify = False).json()
    try:
        return [0, req['sessionId']]
    except:
        return [1,req]

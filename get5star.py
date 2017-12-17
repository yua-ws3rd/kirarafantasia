#import requests
import collections
import json
import urllib3
from str import  *
from requesthash import *
urllib3.disable_warnings()#方便抓包

def get5star(X_STAR_SESSION_ID,goalnum,firstflag = 1):
    api1 = 'player/gacha/draw'
    payload1 = '{"gachaId":1,"drawType":3,"stepCode":0,"reDraw":true}'
    payload2 = '{"gachaId":1,"drawType":3,"stepCode":4,"reDraw":false}'

    urhttp = urllib3.PoolManager()
    star5num = 0
    while star5num < goalnum:
        if firstflag == 1 :#第一次无限十连请求值有所不同，检测选择
            payloadc = payload1
        else:
            payloadc = payload2
            firstflag = 1
        header = collections.OrderedDict(
            [('Unity-User-Agent', 'app/0.0.0; Android OS 7.1.1 / API-25 NMF26F/7.11.16; Xiaomi MI MIX 2'),
             ('X-STAR-REQUESTHASH', getrequesthash(api1, sessionID=X_STAR_SESSION_ID, json1=payloadc)),
             ('X-Unity-Version', '5.5.4f1'),
             ('X-STAR-AB', X_STAR_AB),
             ('X-STAR-SESSION-ID', X_STAR_SESSION_ID),
             ('Content-Type', 'application/json; charset=UTF-8'),
             ('User-Agent', 'Dalvik/2.1.0 (Linux; U; Android 7.1.1; MI MAX 2 MIUI/7.11.16)'),
             ('Host', 'krr-prd.star-api.com'),
             ('Connection', 'Keep-Alive'),
             ('Accept-Encoding', 'gzip')])
        star5num = 0
        #req = requests.session()
        #a = req.post(url1,headers = header,data =payload1 ,verify=False).json() #速度有点慢
        a = urhttp.request('post',api_host+api1,headers=header,body=payloadc)
        try:
            a = json.loads(a.data.decode('utf-8'))
        except:
            print("网络故障，或服务器炸了")
            return ['failed','']
        try:
            b = a['managedCharacters']
        except:
            print("无数据 可能是hash有误")
            return ['failed','']
        d = []
        for c  in b:
            d.append(c['levelLimit'])
        for e in d:
            if e == 50:
                star5num+=1
        print("本轮数量："+str(star5num))
    return ['success',a]

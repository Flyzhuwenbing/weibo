import requests
import random
import pymongo
import time

client = pymongo.MongoClient('localhost',27017)
db = client.weibo
collection = db.comment

headers = {
    'Cookie': 'T_WM=1dbdd7a0fe1f0464a2220438a1d38ae4; ALF=1507381376; SUB=_2A250tTPQDeRhGeRH6FYS9ynIzT-IHXVUVl2YrDV6PUJbktBeLULkkW1PbJn49O4U5wq6-Nz3AzywW4sTkQ..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFHMdfrd-ohyd_fCIO90b3W5JpX5o2p5NHD95QE1KeXe0MNShq0Ws4Dqcj_i--ciK.Ni-27i--NiK.NiK.fi--NiKnpi-8hi--RiK.7i-i2i--ciKLhiKnR; SUHB=0TPV27mbwlU87J; SSOLoginState=1504789377; M_WEIBOCN_PARAMS=featurecode%3D20000320%26oid%3D4145115918944744%26luicode%3D20000061%26lfid%3D4145115918944744%26uicode%3D20000061%26fid%3D4145115918944744',
    'Referer':'https://m.weibo.cn/status/4145115918944744',
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'
}
'''proxy_lst=[
        '183.232.65.203:3128',
        '24.200.102.149:8080',
        '162.243.18.46:3128',
        '119.9.105.210:9000',
        '183.232.65.202:3128',
    ]
proxies = random.choice(proxy_lst).strip()'''
url_comment =['https://m.weibo.cn/api/comments/show?id=4145115918944744&page={}'.format(str(i))for i in range(1,1000)]
def get_comment(url):
    req = requests.get(url,headers = headers)
    content = req.json()
    try:
        for data in content.get('data'):
            comment = {'comment':data.get('text')}
            collection.insert_one(comment)
            print(comment)
    except:
        pass

'''def multi_session(session):
    retryTimes = 10
    while retryTimes > 0:
        try:
            return session.post()
        except:
            print('...')
            retryTimes -= 1'''

for url in url_comment:
    get_comment(url)
    time.sleep(2)






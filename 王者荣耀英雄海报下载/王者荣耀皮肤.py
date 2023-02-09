import os
import json
import urllib.request

if os.path.exists(os.getcwd().replace('\\', '/') + '/' + 'herolist.json') is True:
    os.remove(os.getcwd().replace('\\', '/') + '/' + 'herolist.json')

try:
    urllib.request.urlretrieve('https://pvp.qq.com/web201605/js/herolist.json',
                               os.getcwd().replace('\\', '/') + '/' + 'herolist.json')
except:
    print('下载失败，请自行检查网络连接或下载地址是否有效')

dx = open(os.getcwd().replace('\\', '/') + '/' +
          'herolist.json', encoding='utf-8')
strJson = json.load(dx)


def pdwy(yxname, yxid):
    print(yxname, yxid)
    for i in range(1, 20):
        try:
            downname = yxname + str(i)
            downurl = "https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/" + \
                str(yxid) + "/" + str(yxid) + "-bigskin-" + str(i) + ".jpg"
            urllib.request.urlretrieve(downurl, os.getcwd().replace(
                '\\', '/') + '/' + downname + '.jfif')
        except:
            break


for i in strJson:
    pdwy(i['cname'], i['ename'])

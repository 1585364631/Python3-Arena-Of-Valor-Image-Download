import requests
import os
import json
import logging
import urllib.request


def xiazai(url, name):
    try:
        urllib.request.urlretrieve(url, os.getcwd().replace(
            '\\', '/') + '/' + '壁纸/' + name + '.jfif')
        print(name, ' ------- 下载完成')
    except:
        print(name, ' ------- 下载失败，请自行检查下载地址是否有效')


def chuli(bao):
    try:
        data = json.loads(bao)
        for i in range(0, int(bao.count('sProdName'))):
            lie_bao = data["List"][i]
            for ii in range(1, 9):
                if ii == 2:
                    name = lie_bao["sProdName"] + '1024x768'
                elif ii == 3:
                    name = lie_bao["sProdName"] + '1280x720'
                elif ii == 4:
                    name = lie_bao["sProdName"] + '1280x1024'
                elif ii == 5:
                    name = lie_bao["sProdName"] + '1440x900'
                elif ii == 6:
                    name = lie_bao["sProdName"] + '1920x1080'
                elif ii == 7:
                    name = lie_bao["sProdName"] + '1920x1200'
                elif ii == 8:
                    name = lie_bao["sProdName"] + '1920x1440'
                elif ii == 1:
                    name = lie_bao["sProdName"] + '215x120'
                else:
                    break
                url = lie_bao["sProdImgNo_" + str(ii)]
                url = url[:-3] + '0'
                xiazai(url, name)
                ii += 1
            i += 1
    except:
        chuli(bao)


def zhuabao(url, hear):
    try:
        bao = requests.get(url, hear)
        bao = bao.content
        bao = bao[41:-2]
        bao = bao.decode()
        bao = urllib.request.unquote(bao)
        if bao == '':
            print('出错')
        else:
            try:
                chuli(bao)
            except:
                chuli(bao)
    except:
        zhuabao(url, hear)


if os.path.exists(os.getcwd().replace('\\', '/') + '/' + '壁纸') is False:
    print('检测不到文件夹存在，自动创建')
    os.mkdir(os.getcwd().replace('\\', '/') + '/' + '壁纸')

ye = int(input('请输入共需要下载多少页\n'))

for i in range(0, ye):
    hear = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }
    url = r'https://apps.game.qq.com/cgi-bin/ams/module/ishow/V1.0/query/workList_inc.cgi?activityId=2735&sVerifyCode=ABCD&sDataType=JSON&iListNum=20&totalpage=0&page=' + \
        str(i) + r'&iOrder=0&iSortNumClose=1&jsoncallback=jQuery17106689643651524944_1611131883' + str(485+i) + \
        r'&iAMSActivityId=51991&_everyRead=true&iTypeId=2&iFlowId=267733&iActId=2735&iModuleId=2735&_='
    zhuabao(url, hear)

from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib
import requests
import itchat
import datetime
from apscheduler.schedulers.blocking import BlockingScheduler


def getMessage():
    url = "http://tianqi.sogou.com/shanghai/"
    req = requests.get(url, {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'})
    soup = BeautifulSoup(req.text, 'lxml')
    xml = soup.find("p", {"class": "text"})
    xml1 = soup.find("a", {"class": "date"})
    temperature = soup.find('span', {"class": "temp"})
    umbrella = soup.find_all('span', {"class", "t-right"})
    cy1 = soup.find_all('span', {"class", "info"})
    num = 0
    '''
    msg:天气情况，会不会下雨
    msg1：日期
    temp:温度
    umbrella:是否带伞
    '''
    for i in range(len(xml)):  # 表示从0到xml的len()长度
        msg = xml.string
        msg1 = xml1.string
        temp = temperature.string
        cy = cy1[0].string
        shan = umbrella[1].string
    # print ('小宝贝，今天的天气到啦!','今天是'+msg1,'今天出门'+ shan +'，穿'+ cy, msg+'天，', temp)
    # return ('小宝贝，今天的天气到啦!','今天是'+ msg1 + "日，",'今天出门'+ shan +'，穿'+ cy, msg, temp)
    return '小宝贝，今天的天气到啦!今天是' + msg1 + msg +'天，'+ temp + '，今天出门' + shan + '，穿:' + cy




def timing():
    take_list = [("14:11", weather)]
    for task in take_list:
        task_time = task[0]
        task_concent = task[1]
        if datetime.datetime.now().strftime("%H:%M") == task_time:
            receiver = itchat.search_friends(name=u"海峰")[0]["UserName"]
            itchat.send_msg(task_concent, receiver)
#添加定时任务
def remind_run():
    sched = BlockingScheduler()
    #运行的类，触发
    sched.add_job(timing,'cron',second=0)
    sched.start()

if __name__ == '__main__':
    weather = getMessage()
    print(weather)
    itchat.auto_login(hotReload=True)
    remind_run()
    # weather = getMessage()

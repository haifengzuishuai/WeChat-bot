# -*-coding：utf-8-*-

import itchat
import datetime

from apscheduler.schedulers.blocking import BlockingScheduler
#
task_list = [("20:20", "do A"),
             ("20:21", "do B"),
             ("20:22", "do C")]

def task_remind():
    for task in task_list:
        task_time = task[0]
        task_content = task[1]
        if datetime.datetime.now().strftime("%H:%M") == task_time:
            receiver = itchat.search_friends(name=u"海峰")[0]["UserName"]
            itchat.send_msg(task_content, receiver)


def remind_run():
    sched = BlockingScheduler()
    sched.add_job(task_remind, 'cron', second=0)
    sched.start()


if __name__ == '__main__':
    itchat.auto_login(hotReload=True)
    remind_run()

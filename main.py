#!/usr/bin/env python
#coding:utf-8
"""
file:.py
date:2018/10/15 16:40
author:    peak
description:
"""

from config import engine, Session
from model import Base, Order
import datetime, traceback, time, subprocess




def Query():
    # 查询排队方式为自动排队的订单
    Base.metadata.create_all(engine)
    session = Session()
    All_Order = session.query(Order).filter(Order.Time_Way == 1).all()
    if All_Order:
        for i in range(len(All_Order)):
            if All_Order[i].Print_Status == 1:
                # 尝试下载订单中的文件
                try:
                    cmd = "wget http://rooins.careyou.xin/static/Upload_Files/{} -P ./User_Files/To_Print" .format(All_Order[i].File_Dir)
                    subprocess.call(cmd, shell=True)
                except Exception as e:
                    # 将错误写入下载错误日志
                    print "Error"
                    with open('./log/download_error_log', 'a') as f:
                        f.write(str(datetime.datetime.now()) + " " + All_Order[i].File_Dir + " " + str(e) + "\n")
                else:
                    # 将下载成功写入下载成功日志
                    with open("./log/download_log", "a") as f:
                        f.write(str(datetime.datetime.now()) + " " + All_Order[i].File_Dir + " " + "success-download" + "\n")
                    # 在数据库中做出标记，文件已下载成功
                    All_Order[i].Print_Status = 2
                    print "Ok"
                finally:
                    session.commit()
                    # session.close()
                    # session.flush()
                    print 'close'
    print 'finished'

def Print():

    Base.metadata.create_all(engine)
    session = Session()
    # 将 ./User_Files/To_Print/ 中的文件名导入到预打印日志中
    cmd = "ls ./User_Files/To_Print/ > ./log/ToPrint_filename"
    subprocess.call(cmd)
    ToPrint = open("./log/ToPrint_filename", 'r+')
    for line in ToPrint:
        try:
            # 开始尝试打印
            os.system('lpr ./User_Files/To_Print/{}' .format(line))
        except Exception:
            # 捕获错误，并将错误写入错误日志中
            s = traceback.format_exc()
            with open('./log/print_error_log', 'a') as f:
                f.write(str(datetime.datetime.now()) + " " + s + "\n")
        finally:
            # 将打印成功的文件移动到 ./User_Files/Finished_Print 这个目录中
            os.system('mv ./User_Files/To_Print/{} ./User_Files/Finished_Print' .format(line))

            # 在数据库中修改打印状态为2，表示已经打印
            printed_order = session.query(Order).filter(Order.File_Dir == line)
            printed_order.Print_Status = 2
            session.commit()
            session.close()

            # 在./log/print_access_log 中写入打印成功日志
            with open('./log/print_access_log', 'a') as f:
                f.write(str(datetime.datetime.now()) + " " + line + "success-printed")

while 1:
    Query()
    time.sleep(5)
    # Print()






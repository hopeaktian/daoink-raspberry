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
import datetime, os, traceback


Base.metadata.create_all(engine)
session = Session()

def Query():
    # 查询排队方式为自动排队的订单
    All_Order = session.query(Order).filter(Order.Time_Way == 1).all()
    for i in range(len(All_Order)):
        if All_Order[i].Print_Status == 1:
            # 尝试下载订单中的文件
            try:
                os.system('wget http://rooins.careyou.xin/static/Upload_Files/{} -P ./User_Files/To_Print' .format(All_Order[i].File_Dir))
            except Exception:
                # 将错误写入下载错误日志
                s = traceback.format_exc()
                with open('./log/download_error_log') as f:
                    f.write(str(datetime.datetime.now()) + " " + s + "\n")
            finally:
                # 将下载成功写入下载成功日志
                with open("./log/download_log", "w") as f:
                    f.write(str(datetime.datetime.now()) + " " + All_Order.File_Dir + "\n")

def Print():

    # 将 ./User_Files/To_Print/ 中的文件名导入到预打印日志中
    os.system('ls ./User_Files/To_Print/ > ./log/ToPrint_filename')
    ToPrint = open("./log/ToPrint_filename")
    for line in ToPrint:
        try:
            # 开始尝试打印
            os.system('lpr ./User_Files/To_Print/{}' .format(line))
        except Exception:
            # 捕获错误，并将错误写入错误日志中
            s = traceback.format_exc()
            with open('./log/print_error_log') as f:
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
            with open('./log/print_access_log') as f:
                f.write(str(datetime.datetime.now()) + " " + line + "success")

while 1:
    Query()
    Print()






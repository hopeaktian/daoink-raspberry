#!/usr/bin/env python
#coding:utf-8
"""
file:.py
date:2018/10/15 11:37
author:    peak
description:
            对软件的配置
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# 配置数据库连接, 请修改一下四个变量为自己数据库的配置信息,即可。
DB_USER = "user"                        # 数据库用户名
DB_PASSWORD = "password"                # 数据库密码
DB_HOST = "localhost"                   # 数据库主机
DB_NAME = "test"                        # 数据库名



engine = create_engine('mysql+pymysql://{}:{}@{}:3306/{}' .format(DB_USER, DB_PASSWORD, DB_HOST, DB_NAME))
Session =sessionmaker(bind=engine)
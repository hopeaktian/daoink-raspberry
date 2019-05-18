#coding=utf-8
from check_usb import check_usb
import redis
import time
from config import Printer_grep, RedisConfig

def status_sync(device_name):
    status = check_usb(device_name)
    check_time = int(time.time())
    r = redis.Redis(host=RedisConfig.host, password=RedisConfig.password, port=RedisConfig.port, db=0, decode_responses=True)
    if r.exists('test_printer'):
        r.lset("test_printer", 0, status)
        r.lset("test_printer", 1, check_time)
    else:
        r.rpush("test_printer", status)         # pinter status
        r.rpush("test_printer", check_time)     # check time
        r.rpush("test_printer", None)           # device useable status

while True:
    status_sync(Printer_grep)
    time.sleep(2)

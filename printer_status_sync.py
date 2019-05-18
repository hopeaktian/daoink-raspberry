#coding=utf-8
from check_usb import check_usb
import redis
import time


def status_sync(device_name):
    status = check_usb(device_name)
    check_time = int(time.time())
    r = redis.Redis(host='60.205.176.255', password='Blqrwuzg3', port=6379, db=0, decode_responses=True)
    r.rpush("test_printer", status)
    r.rpush("test_printer", check_time)

while True:
    status_sync()
    time.sleep(1)

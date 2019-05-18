#!/usr/bin/env python
import subprocess

def check_usb(usb_device_name):
    cmd = "lsusb | grep {} | wc -l" .format(usb_device_name)
    p1 = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    output = p1.communicate()[0]
    return int(output)


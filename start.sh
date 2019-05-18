#! /bin/bash
. ./env/bin/activate
nohup python main.py &
nohup python printer_status_sync.py &
echo "start rooins-Raspberry success"
#!/bin/bash
ps aux | grep main.py | grep -v color | awk '{print $2}'| xargs kill -12
echo "Stoped rooins-Raspberry"
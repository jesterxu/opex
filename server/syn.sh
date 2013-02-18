#!/bin/sh
# SYN listeliyoruz
netstat -ntu |grep SYN | awk '{print $5}' | awk '{sub("::ffff:","");print}' | cut -f1 -d ':' | sort | uniq -c | sort -n | grep -v -e server -e Address -e 127.0.0.1 -e 0.0.0.0
#! usr/bin/python3

import os
import socket

user='your username'
ip='ypur ip list or you can read the file with ip's'
ip_list=ip.replace(' ','').split(',')
#hosts = open('/etc/hosts','r')
hostname = socket.gethostname()
my_host=(socket.gethostbyname(hostname))
#print(ip_list)
for i in ip_list:
    if i != my_host:
       b = os.system('<path to script>/post-receive.sh' + ' ' + i )

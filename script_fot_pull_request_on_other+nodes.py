#!/usr/bin/python3

import socket
import subprocess


user='<username>'
ip='<some ip>, <some ip>, <some ip>'
ip_list=ip.replace(' ','').split(',')
#hosts = open('/etc/hosts','r')
hostname = socket.gethostname()
my_host=(socket.gethostbyname(hostname))
#print(ip_list)
for i in ip_list:
    if i != my_host:
        sshProcess = subprocess.Popen(['ssh', i], stdin=subprocess.PIPE, 
                               stdout = subprocess.PIPE,
                               universal_newlines=True,
                               bufsize=0)
        sshProcess.stdin.write("cd $HOME/git/projects/\n")
        sshProcess.stdin.write("git pull origin master\n")
        sshProcess.stdin.close()

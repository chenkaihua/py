#!/usr/bin/env python

import os

def get_ip_address (line):
    pass
def get_host_name(line):
    pass

f = open('/home/kaihua/www/scripts/kaihua_hosts', 'r')
#print(f.read())
for line in f.readline():
    #print(line.strip())
    #print(line.split(' ', 1)) 
    pass
f.close()

class host():
    
    def __init__(self, name, ip, os, comments):
        self.name = name 
        self.ip = ip
        self.os = os
        self.comments = comments
    
    def ping_test(self):
        respone = os.system("ping -c 3 " + self.ip)
        print(respone)
        if respone == 0:
            print("The server is alive")
        else:
            print("Server is unaccessible")

    def show_hosts (self):
        print(self.name + '\t'+ self.ip + '\t' + "# " + self.os + '\t' + self.comments)

#if __name__ ==' __main__':
sgh28h7 = host('sgh28h7', '10.103.117.90', 'SunOS', "Will decomission soon")
sgh28h7.ping_test()
sgh28h7.show_hosts()

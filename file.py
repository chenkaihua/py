#!/usr/bin/env python

import os
import re

class host():
    
    def __init__(self, name, ip, comments):
        self.name = name 
        self.ip = ip
        self.comments = comments
    
    def ping_test(self):
        respone = os.system("ping -c 3 " + self.ip)
        if respone == 0:
            print("The server is alive")
        else:
            print('self.name is unaccessible')

    def show_hosts (self):
        print(self.name + '\t'+ self.ip + '\t' + "# " + self.comments)

class host_array_class():
    def __init__(self, host_array, result_file):
        self.host_array = host_array
        self.result_file = result_file
    
    def host_update(self):
        date = os.system("date")
        self.result_file.write(str(date))
        for host in host_array:
            respone = os.system("ping -c 3 " + host.ip)
            if respone == 0:
                pass
            else:
                self.result_file.write(str(host.show_hosts())
                self.result_file.write(" is unaccessible\n")

if __name__=="__main__":
    result_file = open('/tmp/kaihua_host_check_python', 'w')
    f = open('/home/kaihua/www/scripts/kaihua_hosts', 'r')
    host_array=[]

    for line in f:
        if (re.search('^#', line)):
            continue
        if (re.search('^$', line)):
            continue

        server=host(line.split()[1], line.split()[0], line.split('#')[1])
        host_array.append(server)

    kaihua_hosts=host_array_class(host_array, result_file)
    kaihua_hosts.host_update()

    result_file.close()
    f.close()

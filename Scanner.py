# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 11:25:04 2021

@author: okazm
"""

import threading
from socket import *
import pyprind


N = 2 ** 16 - 1
ip = input('Введите IP: ')


def scan_port(ip, port):
    global z
    sock = socket(AF_INET, SOCK_STREAM)
    sock.settimeout(0.5)
    try:
        sock.connect((ip, port))
        if port!=0:
            z.append(port)
        #print('\n',"Порт", port, "открыт")
        sock.close()
    except:
        pass
bar = pyprind.ProgBar(N)
z=[]
for i in range(N):
    thr = threading.Thread(target=scan_port, args=(ip, i))
    thr.start()
    bar.update()
for i in z:
    print('Порт', i, 'открыт')


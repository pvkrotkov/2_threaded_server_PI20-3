import threading
import socket
import time
import pyprind

ip = input('Введите адрес (Пример: www.fa.ru или 127.0.0.1): ')
ports = []
i = 2 ** 16 - 1
bar = pyprind.ProgBar(i)


def scan(ip, port):
    global ports
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(.5)
    try:
        sock.connect((ip, port))
        ports.append(port)
        sock.close()
    except:
        pass


for port in range(i):
    if port in ports:
        continue
    thread = threading.Thread(target=scan, args=(ip, port))
    thread.start()
    bar.update()


print('Список открытых портов:', ports)

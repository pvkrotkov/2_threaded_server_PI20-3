import socket
import threading
import pyprind
N = 2 ** 16 - 1
ip = 'localhost'

def scan_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    try:
        sock.connect((ip, port))
        print('\n',"Порт", port, "открыт")
        sock.close()
    except:
        pass
bar = pyprind.ProgBar(N)
for i in range(N):
    potoc = threading.Thread(target=scan_port, args=(ip, i))
    potoc.start()
    bar.update()

import socket
import threading
import pyprind

N = 65536

Progress = pyprind.ProgBar(N)

ip = '192.168.0.1'

def scan_port(ip,port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    try:
        connect = sock.connect((ip,port))
        print(f'\nport {port} is open')
        sock.close()
    except:
        pass
    finally:
        Progress.update()

if __name__ == '__main__':
    [threading.Thread(target=scan_port, args=(ip, i)).start() for i in range(N)]

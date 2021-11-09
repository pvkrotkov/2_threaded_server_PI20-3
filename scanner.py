import pyprind, threading
import socket



number_of_all_ports = 2 ** 16 - 1
ip = input('Введите IP: ')


def scanning(ip, port):
    global opened_ports
    sock = socket.socket()
    sock.settimeout(0.25)
    try:
        sock.connect((ip, port))
        if port!=0:
            opened_ports.append(port)
        sock.close()
    except:
        pass

progress_bar = pyprind.ProgBar(number_of_all_ports)

opened_ports=[]

for i in range(number_of_all_ports):
    p1 = threading.Thread(target=scanning, args=(ip, i))
    p1.start()
    
   
    

    progress_bar.update()

for port in opened_ports:
    print(f'Порт {port} открыт')

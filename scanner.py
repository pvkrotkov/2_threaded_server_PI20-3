import socket
import threading
import time
from tqdm import tqdm  # python -m pip install tqdm

ip = input('Введите адрес (Пример: www.fa.ru или 127.0.0.1): ')
ports = []
i = 1000

try:
    def scan(ip, port):
        global ports
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(.05)
        try:
            sock.connect((ip, port))
            print('Порт', port, 'открыт')
            ports.append(port)
            sock.close()
        except:
            pass

    def p_port():
        for port in tqdm(range(i)):
            if port in ports:
                continue
            thread = threading.Thread(target=scan, args=(ip, port))
            thread.start()
            time.sleep(.01)

    print('Список открытых портов:', ports)


    th2 = threading.Thread(target=p_port, name='open')
    th2.start()
    th2.join()


except ValueError:
    print('Ошибка при вводе данных. Попробуйте ещё раз')

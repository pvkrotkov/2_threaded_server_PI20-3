import socket
import threading
import time
from tqdm import tqdm  # python -m pip install tqdm

ip = input('Введите адрес (Пример: www.fa.ru или 127.0.0.1): ')
ports = []

try:
    i = int(input('Введите кол-во портов, у которых будет проверена возможность подключения: '))


    def scan(ip, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(.05)
        try:
            sock.connect((ip, port))
            print('Порт', port, 'открыт')
            ports.append(port)
            sock.close()
        except:
            pass


    for port in tqdm(range(i)):
        thread = threading.Thread(target=scan, args=(ip, port))
        thread.start()
        time.sleep(.05)

    print('Список открытых портов:', ports)
    
except ValueError:
    print('Ошибка при вводе данных. Попробуйте ещё раз')

#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import socket
from concurrent.futures import ThreadPoolExecutor
import tqdm

def scan_port(host, port, progress_bar, ports):
    sock = socket.socket() #создаем сокет
    sock.settimeout(0.3)
    try:
        sock.connect((host, port)) #пытаемся подключиться к порту
        ports.append(port)
    except:
        pass
    progress_bar.update()


host = input('Введите адрес: ')
start_port = int(input('Введите минимальный порт: '))
end_port = int(input('Введите максимальный порт: '))
thread = int(input('Введите количество потоков, которые нужно использовать для сканирования одновременно: '))



open_ports = [] #список открытых портов
progress_bar = tqdm.tqdm(total=end_port-start_port+1)

with ThreadPoolExecutor(thread) as executor: #создание исполнительного блока экземпляра ThreadPoolExecutor, который будет быстро очищать потоки после завершения работы
    futures = []
    for port in range(start_port, end_port+1):
        future = executor.submit(scan_port, host, port, progress_bar, open_ports) #возвращает объект future из futures
        futures.append(future)
    for future in futures:
        future.result() #Вызываем для всех отправленных вызовов, чтобы программа не пропустила никаких исключений функции.

progress_bar.close()


for port in open_ports:
    print(f'Port {port} is opened!')
    


# In[ ]:





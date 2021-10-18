import socket, threading, time
from progress.bar import IncrementalBar #необходимо установить модуль Progress (pip install progress)

# функция для сканирования порта
def scan_p(ip,port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.1)
    try:
        sock.connect((ip,port))
        print(f" ------ Порт {port} открыт ------")
        sock.close()
    except:
        pass

#N = 2**16 - 1 - максимальное количество возможных портов

ip = input('Введите ваш IP-адрес(пример 127.0.0.1): ')
i = 1000   #кол-во портов, у которых будем проверять возможность подключения
bar = IncrementalBar('Countdown', max = i) #объявляем объект Progress Bar с максимальной выборкой max

# запускаем цикл по портам и создаем каждый раз новый поток для соотв. порта
for port in range(i):
    thread = threading.Thread(target=scan_p, args=(ip,port))
    thread.start()

    bar.next()#запуск progress bar
    time.sleep(0.1)
    
bar.finish()
    
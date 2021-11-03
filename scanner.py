import socket, threading, time
from progress.bar import IncrementalBar #pip install progress

#N = 2**16 - 1 (максимальное кол-во возможных портов)
ports=[]

def scan_p(ip,port): #сканируем порт
    global ports
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.1)
    try:
        sock.connect((ip,port))
        sock.close()
        ports.append(port)
    except:
        pass

def print_port():               
        for p in range(i):  # цикл подключенных клиентов, создает соответствующий поток
            if p in ports: # если поток уже существует, то пропускаем
                continue
            index = threading.Thread(target = scan_p,args = (ip,p))
            index.start()
        if len(ports)>=1:
            print('\n',"Количество открытых портов: ",len(ports))
            print('Порты:')
            for port in ports:
                print(port)
        else:
            print('\n','Нет открытых портов')

ip = input('Введите ваш IP-адрес(пример 127.0.0.1): ')
i = 1000   #задаем кол-во портов, у которых будем проверять возможность подключения
bar = IncrementalBar('Countdown', max = i) #объявляем объект Progress Bar

for port in range(i):  # запускаем цикл по портам и создаем каждый раз новый поток для соотв. порта
    thread = threading.Thread(target=scan_p, args=(ip,port))
    thread.start()

    bar.next() #запускаем progress bar

th2 = threading.Thread(target=print_port, name='open')
th2.start()
th2.join()

bar.finish()

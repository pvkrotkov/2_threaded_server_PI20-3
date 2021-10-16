import socket
import time
import sys
from threading import Thread


STEP = 66 # каждому потоку будем отводить 66 портов
#         66 - чтобы обработать тысячу портов 15 потоками - рекоммендованное число
open_ports = []
threads = []
address = input('Введите адрес для проверки портов: ')


def scan(address, ports):
    global STEP
    for port in ports:
        #print(f'Сканируем порт №{port}...')
        try:
            socket.socket().connect((address, port))
            global open_ports
            open_ports.append(port)
            #print(f'ОТКРЫТО! - порт №{port}!!!')
        except:
            #print(f'Порт №{port} закрыт.')
            continue
    #print(f'Поток №{ports[0]//STEP+1} работу завершил!')


# настройка прогресс бара
toolbar_width = 40
sys.stdout.write("[%s]" % (" " * toolbar_width))
sys.stdout.flush()
sys.stdout.write("\b" * (toolbar_width+1))


for port in range(1,1001,STEP):
    threads.append(Thread(target = scan, args=(address, [numb for numb in range(port, port+STEP)]))) # помещаем поток в список, чтобы отслеживать их завершение
    threads[port//STEP].start() # запускаем поток


# внешний цикл для работы прогресс-бара, внутренний - алгоритм
for i in range(toolbar_width):
    time.sleep(0.1)

    # ожидаем завершения работы всех потоков
    while len(threads)>0:
        for i in range(len(threads)-1,-1,-1):
            if not threads[i].is_alive():
                threads.remove(threads[i])

    sys.stdout.write("-")
    sys.stdout.flush()

sys.stdout.write("\n")

print('Открытые порты: ', end='')
for port in sorted(open_ports):
    print(port, end=' ,')

print(f'.\nВсего: {len(open_ports)}.')

import socket
import threading

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while True:
    nickname = input ('Enter your nickname: ')
    if 1<len(nickname)<20:
        break

sock.connect(('localhost', 9091)) 


def sending():
    # Функция передачи data к серверу
    sock.send(f'client {nickname} joined'.encode())
    while True:
        mes = (input())
        sock.send(f'{nickname}: {mes}'.encode())
        
        if mes=='exit':
            sock.close()   
            break     
        


def receiving():
    # Функция получения echo от сервера
    while True:   
        try:   
            data = sock.recv(1024)
            print(data.decode())
        except:
             print('Отключение')
             break

t1 = threading.Thread(target=sending, name='sending')
t2 = threading.Thread(target=receiving, name='receiving')

t1.start()
t2.start()

t2.join()


sock.close()

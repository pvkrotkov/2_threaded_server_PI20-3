
import socket, threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = input('Целевой IP-адрес входа: ')
 
while True:
    name = input ('Введите личный ник (1<длина<10): ')
    if 1<len(name)<10:
        break
 
port = 9090
 

client.connect((host, port))
print ('-' * 5+ 'подключился к серверу' + '-' * 5)
print ('-' * 5 + 'Enter, чтобы закрыть соединение с сервером' + '-' * 5)
 
 
def outdatas():
    while True:
        outdata = input('')
        print()
        if outdata=='enter':
            break
                
        client.send(f'{name}: {outdata}'.encode('utf-8'))
        print('%s:%s'% (name, outdata))
 
 
def indatas():
 
    while True:
        try:
            indata = client.recv(1024)
            print(indata.decode('utf-8'))
        except:
            print('--Отключение--')
            break
 
t1 = threading.Thread(target=indatas, name='input')
t2 = threading.Thread(target=outdatas, name='out')
 
t1.start()
t2.start()

t2.join()

print ('-' * 5 + 'сервер отключен' + '-' * 5)
client.close()
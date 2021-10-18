import socket, threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
print(f'Сервер: {host}')
server.bind((host, 9090))
server.listen(5)

print ('Enter для выхода с сервера')

 # Создайте список клиентов
clients = list()
 # Хранить клиентов, которые создали потоки
end = list()

 # Блокировка ожидания подключения клиента, возврата объекта подключения и адреса косвенного объекта
def accept():
    while True:
        client, addr = server.accept()
        clients.append(client)
        print ('-' * 2 + f'сервер подключен через {addr}: текущее количество подключений: -- {len (clients)}' + '-' * 2, end = '')


def recv_data(client):
    while True:
                 # Принимаем информацию от клиента
        try:
            indata = client.recv(1024)
        except:
            clients.remove(client)
            end.remove(client)
            print ('-' * 2 + f'Сервер отключен: текущее количество подключений: -- {len (clients)}' + '-' * 2, end = '')
            break
        print(indata.decode('utf-8'))
        for clien in clients:
            # Перенаправить информацию от клиента и отправить ее другим клиентам
            if clien != client:
                clien.send(indata)
 
def outdatas():
    while True:
        # Введите информацию, которая будет предоставлена ​​клиенту
        print('')
        outdata = input('')
        print()
        if outdata=='enter':
            break
            print ('Отправить всем: % s'% outdata)
        # Отправлять информацию каждому клиенту
        for client in clients:
            client.send (f"Сервер: {outdata}". encode ('utf-8)'))
 
 
def indatas():
    while True:
                 # Выполните цикл подключенных клиентов и создайте соответствующий поток
        for clien in clients:
            # Если поток уже существует, пропустить
            if clien in end:
                continue
            index = threading.Thread(target = recv_data,args = (clien,))
            index.start()
            end.append(clien)
 
 
 # Создать многопоточность
 # Создать получающую информацию, объект потока
t1 = threading.Thread(target = indatas,name = 'input')
t1.start()
 
 # Создать отправляемое сообщение, объект потока
 
t2 = threading.Thread(target = outdatas, name= 'out')
t2.start()
 
 # Ожидание подключения клиента, объект потока
 
t3 = threading.Thread(target = accept(),name = 'accept')
t3.start()
 
 # Блокировать округ, пока подпоток не будет завершен, и основной поток не может закончиться
# t1.join()
t2.join()
 
 # Выключите все серверы
for client in clients:
    client.close()
print ('-' * 2 + 'сервер отключен' + '-' * 2)



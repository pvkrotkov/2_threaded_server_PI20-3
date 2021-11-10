import socket
import socket, threading

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(0)
conn, addr = sock.accept()
print(addr)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

msg = ''
host = socket.gethostname()
print(f'Сервер: {host}')
server.bind((host, 9090))
server.listen(5)

while True:
	data = conn.recv(1024)
	if not data:
		break
	msg += data.decode()
	conn.send(data)
print ('Enter для выхода с сервера')

clients = list()
end = list()


def accept():
    while True:
        client, addr = server.accept()
        clients.append(client)
        print ('-' * 2 + f'сервер подключен через {addr}: текущее количество подключений: -- {len (clients)}' + '-' * 2, end = '')


def recv_data(client):
    while True:
        try:
            indata = client.recv(1024)
        except:
            clients.remove(client)
            end.remove(client)
            print ('-' * 2 + f'Сервер отключен: текущее количество подключений: -- {len (clients)}' + '-' * 2, end = '')
            break
        print(indata.decode('utf-8'))
        for clien in clients:
            if clien != client:
                clien.send(indata)

def outdatas():
    while True:
        print('')
        outdata = input('')
        print()
        if outdata=='enter':
            break
            print ('Отправить всем: % s'% outdata)
        for client in clients:
            client.send (f"Сервер: {outdata}". encode ('utf-8)'))


def indatas():
    while True:
        for clien in clients:
            if clien in end:
                continue
            index = threading.Thread(target = recv_data,args = (clien,))
            index.start()
            end.append(clien)

t1 = threading.Thread(target = indatas,name = 'input')
t1.start()

t2 = threading.Thread(target = outdatas, name= 'out')
t2.start()

t3 = threading.Thread(target = accept(),name = 'accept')
t3.start()

t2.join()

for client in clients:
    client.close()
print ('-' * 2 + 'сервер отключен' + '-' * 2)

print(msg)

conn.close()
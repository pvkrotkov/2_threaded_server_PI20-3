import socket
import threading

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 9091)) 
sock.listen(5)  # максимальное количество клиентов 




def connect(sock):
    # Функция принятия подключения клиента
    while True:
        conn, addr = sock.accept()
        print(f'Client joined. Addres {addr}')
        if conn is not None:
            new_client(conn) 
    
def new_client(conn):
    global dict_of_clients
    name = conn.recv(1024)
    name = name.decode()
    conn.send('Echo from server'.encode())
    output(conn)
    
def output(conn):
    while True:
        data = conn.recv(1024)  
        print(data.decode())


while True:
    threads = [threading.Thread(target=connect, args=[sock]) for _ in range(3)]
    [thread.start() for thread in threads]
    [thread.join() for thread in threads]

import socket

sock = socket.socket()
sock.bind(('', 7777))
sock.listen(0)
conn, addr = sock.accept()
print(addr)

msg = ''

while msg !='exit':
    data = conn.recv(1024)
    msg = data.decode()
    print(msg)
    conn.send(data)

conn.close()

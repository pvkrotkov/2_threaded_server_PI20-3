import socket

sock = socket.socket()
sock.setblocking(1)
sock.connect(('10.4.200.245', 6666))
msg = "Hi!"
while msg != 'exit':
    msg = input()
    sock.send(msg.encode())
    data = sock.recv(1024)

sock.close()

print(data.decode())

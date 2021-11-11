# coding=utf-8
import threading
import socket


def scanp(port):
    global r
    p1 = port * 1024
    p2 = p1 - 1024
    for i in range(p2, p1):
        sock = socket.socket()
        sock.settimeout(0.5)
        if i == r - 1:
            print ("Сканирование завершено!")
        try:
            connection = sock.connect(('127.0.0.1', i))
            print( i, "открыт.")
            connection.close()
        except:
            # print(i)
            pass


s = 4  # Введите число s от 1 до 64.  1 = 1024, 64 = 65536
r = s * 1024
print ("Запущено сканирование " + str(r) + " портов")
for element in range(s + 1):
    t = threading.Thread(target=scanp, kwargs={'port': element})
    t.start()

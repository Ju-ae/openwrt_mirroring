import socket

HOST= '192.168.1.1'
PORT = 1234
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))
while 1 :
    a = input()
    if a == "exit" :
        break
    s.send(bytes(a, encoding = "ascii"))
    data = s.recv(1024)
s.close()
print('Received', repr(data))

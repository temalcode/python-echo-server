import socket

c = socket.socket()
c.connect(('localhost', 3333))
print(c.recv(1024).decode())

while True:
    userInput = input('Enter something: ')
    c.send(bytes(userInput, 'utf-8'))
    print('Server: ' + c.recv(1024).decode())

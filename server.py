import socket

s = socket.socket()
s.bind(('localhost', 3333))
s.listen(1)
print('server is listening')

c, addr = s.accept()
print('Connected: ' + str(addr))
c.send(bytes('Welcome to the echo server. Send me something, I will send it back to you.', 'utf-8'))

while True:
    userInput = c.recv(1024).decode()
    c.send(bytes(userInput, 'utf-8'))

import socket

server_socket = socket.socket()
print('Socket Created')
server_socket.bind(('localhost', 9999))
server_socket.listen(3)
print('Waiting for connections')

while True:
    client_socket, address = server_socket.accept()
    name = client_socket.recv(1024).decode()
    print('Connected with', address,name)
    client_socket.send(bytes(f'Welcome {name}!', 'utf-8'))
    client_socket.close()
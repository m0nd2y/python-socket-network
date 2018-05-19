import socket

while 1:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 8000))
    server_socket.listen(0)
    client_socket , addr = server_socket.accept()
    data = client_socket.recv(65535)
    client_socket.send(data)
    print ( "Recieved Data : " , data.decode() )

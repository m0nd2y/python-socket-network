import socket
import time
while 1:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('127.0.0.1', 8000))
    a = input()
    sock.send(a.encode())
    data= sock.recv( 65535 )
    print( "데이터를 돌려받았다 : ", data.decode())

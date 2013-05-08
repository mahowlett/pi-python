# gpio server test client program
import socket,sys

HOST = '192.168.1.4'    # The remote host
PORT = 50007            # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
arg = sys.argv[1]
s.connect((HOST, PORT))
s.sendall(bytes(arg,'UTF-8'))
data = s.recv(1024)
s.close()
print('Received', data)

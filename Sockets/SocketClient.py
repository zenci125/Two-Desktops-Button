import socket # TODO: make it so client opens a socket once and is connected until server is terminated

host = 'daring.cwi.nl'
port = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.sendall('N')

s.close()

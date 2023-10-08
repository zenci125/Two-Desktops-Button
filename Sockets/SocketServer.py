import socket # TODO: server should run only when the desktop is booted up, on exit the server should be terminated

host = ''
port = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET, SOCK_STREAM - constants, represent adress families and represent the socket types respectively
s.bind((host, port)) # binds the socket with the address, requests tuple type
s.listen(1) # listens for number of connections
connection, address = s.accept() # accept a connection
while 1:
    data = connection.recv(1) # socket recieves data from client. Only recieves a Y / N signal in this instance
    if data == 'N':
        break
    connection.sendall(data)

connection.close() # terminate client connection
socket.close() # terminate server

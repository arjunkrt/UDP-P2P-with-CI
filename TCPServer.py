from socket import *

serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
#In the line below give the local IP address of
#the machine if the clients and server are in the same network.
serverSocket.bind(("192.168.1.9",serverPort))
serverSocket.listen(1)
print("The server is listening")
while 1:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024)
    print(sentence)
    connectionSocket.close()
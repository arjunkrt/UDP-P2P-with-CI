from socket import *

serverName = "192.168.1.10"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
sentence = input("Enter the client no")
clientSocket.send(sentence.encode())
serverack = clientSocket.recv(1024)
rfc_no = input(serverack.decode())
clientSocket.send(rfc_no.encode())
while 1:#a condition, such as whether you got the RFC you wanted
    clientSocket.send(sentence.encode())#the receiving process
clientSocket.close()
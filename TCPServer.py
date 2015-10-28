from socket import *

serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
#In the line below give the local IP address of
#the machine if the clients and server are in the same network.
serverSocket.bind(("192.168.1.10",serverPort))
#number of concurrent connections allowed
no = input("Enter the maximum number of clients allowed")
print(no)
serverSocket.listen(int(no))
print("The server is listening")
var = 0
while 1:
    connectionSocket, addr = serverSocket.accept()
    #var+=1
    #print("No of connections :",var)
    sentence = connectionSocket.recv(1024)
    print(sentence.decode())
    ack = "CONNECTION ESTABLISHED. ENTER RFC NO"
    connectionSocket.send(ack.encode())
    rfcno = connectionSocket.recv(1024)
    print("requested rfc :",rfcno.decode())
connectionSocket.close()
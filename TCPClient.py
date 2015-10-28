from socket import *


class TCPClient(object):
    serverName = "192.168.1.10"
    serverPort = 7734
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))

    def frameMessage(self):
        input_list = []
        while 1:
            stro = input(">")
            if stro == "":
                break
            else:
                input_list.append(stro)
        message = ""
        for i in input_list:
            message = message + i + "|"
        return message

client = TCPClient()
mesg = client.frameMessage()
client.clientSocket.send(mesg.encode())
while 1:  # a condition, such as whether you got the RFC you wanted
    pass  # the receiving process
    client.clientSocket.close()

    """

    ADD RFC 2345 P2P-CI/1.0
    Host: thishost.csc.ncsu.edu
    Port: 5678
    Title: Domain Names and Company Name Retrieval

    LOOKUP RFC 3457 P2P-CI/1.0
    Host: thishost.csc.ncsu.edu
    Port: 5678
    Title: Requirements for IPsec Remote Access Scenarios

    LIST ALL P2P-CI/1.0
    Host: thishost.csc.ncsu.edu
    Port: 5678
    """

from socket import *
from p1 import Lists
import _thread

class TCPServer(object):

    serverPort = 7734
    serverSocket = socket(AF_INET,SOCK_STREAM)

    serverSocket.bind(("192.168.1.10",serverPort))
    serverSocket.listen(1)
    print("The server is listening")
    peerList = None
    RFCList = None
    def processAddRequest(self,peersocket,addr,commandlines):
        """Sample ADD
        ADD RFC 2345 P2P-CI/1.0
        Host: thishost.csc.ncsu.edu
        Port: 5678
        Title: Domain Names and Company Name Retrieval
        """
        line1 = commandlines[0]
        line4 = commandlines[3]
        rfcno = line1.split()[2]
        ipaddr = addr[0]
        #global
    def processLookupRequest(self,peersocket,addr,commandlines):
        pass
    def processListRequest(self,peersocket,addr,commandlines):
        pass
    def threadPerClient(self,peersocket,addr):
        command = peersocket.recv(4096)
        decodedCom = command.decode()
        """
        processing the command starts here
        """
        commandlines = decodedCom.split("|")
        firstline = commandlines[0]
        method = firstline.split()
        if method=="ADD":
            self.processAddRequest(peersocket,addr,commandlines)
        elif method=="LOOKUP":
            self.processLookupRequest(peersocket,addr,commandlines)
        elif method=="LIST":
            self.processListRequest(peersocket,addr,commandlines)
        else:
            pass#decide what to do here. Unsupported operation
        """
        processing the command ends here
        """
        peer = Lists.LLNodePeer()
        peer.set_ipaddr(addr[0])
        peer.set_portno(int(addr[1]))
        #global peerList
        #global RFCList
        if TCPServer.peerList is None:
            peerList = Lists.LLPeer(peer)
        else:
            TCPServer.peerList.add(peer)
        while 1:
            data = peersocket.recv(1024)
            if not data:
                break
            peersocket.send("REQUESTED RFC".encode())
        peersocket.close()
    def printPeerList(self):
        if peerList is None:
            print("NO ACTIVE PEERS")
        else:
            current = peerList.head
            while current is not None:
                print("-->"),
                print(current.get_ipaddr(),current.get_portno(), sep=" "),
                current = current.get_next()
        return
    def printRFCList(self):
        if RFCList is None:
            print("NO RFC's")
        else:
            current = RFCList.head
            while current is not None:
                print("-->"),
                print(current.get_rfcno(),current.get_rfcname(),current.get_ipaddr,sep=" "),
                current = current.get_next()
        return

server = TCPServer()
while 1:
    connectionSocket, addr = server.serverSocket.accept()
    print("INCOMING CLIENT",addr)
    _thread.start_new_thread(server.threadPerClient, (connectionSocket,addr))
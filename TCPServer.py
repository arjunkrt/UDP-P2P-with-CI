from socket import *
from p1 import Lists
from p1 import RFCLists
import _thread


list_of_peers = []
list_of_rfcs = []
class TCPServer(object):

    serverPort = 7734
    no_of_clients = 0;
    serverSocket = socket(AF_INET,SOCK_STREAM)

    serverSocket.bind(("192.168.1.10",serverPort))
    serverSocket.listen(10)
    print("The server is listening")

    def threadPerClient(self,peersocket,addr):
        global list_of_peers
        global list_of_rfcs
        while 1:
            command = peersocket.recv(4096)
            if command:
                decodedCom = command.decode()
                commandlines = decodedCom.split("|")
                firstline = commandlines[0]
                method = firstline.split()[0]

                if method=="ADD":
                    #ADD RFC 2345 P2P-CI/1.0
                    #Host: thishost.csc.ncsu.edu
                    #Port: 5678
                    #Title: Domain Names and Company Name Retrieval
                    peerPresent = False
                    for a in range(0,len(list_of_peers)):
                        peer = list_of_peers[a]
                        if peer.ipaddr == addr[0]:
                            peerPresent=True
                            break

                    if peerPresent is False:
                        peer = Lists.LLNodePeer()
                        peer.set_ipaddr(addr[0])
                        peer.set_portno(int(addr[1]))
                        list_of_peers.append(peer)
                    print("PEER LIST SIZE",len(list_of_peers))

                    line1 = commandlines[0]
                    line4 = commandlines[3]
                    rfcno = line1.split()[2]
                    ipaddr = addr[0]
                    rfcname = line4.split()[1:]
                    rfcname = " ".join(rfcname)
                    rfc = RFCLists.LLNodeRFC()
                    rfc.xset_ipaddr(ipaddr)
                    rfc.xset_rfcname(rfcname)
                    rfc.xset_rfcno(int(rfcno))

                    list_of_rfcs.append(rfc)
                    print("RFC LIST SIZE",len(list_of_rfcs))

                elif method=="LOOKUP":
                    #LOOKUP RFC 3457 P2P-CI/1.0
                    #Host: thishost.csc.ncsu.edu
                    #Port: 5678
                    #Title: Requirements for IPsec Remote Access Scenarios

                    line1 = commandlines[0]
                    rfcno = line1.split()[2]
                    rfcno = int(rfcno)
                    rfcholders = []
                    for i in range(0,len(list_of_rfcs)):
                        obj = list_of_rfcs[i]
                        if obj.rfcno == rfcno:
                            rfcholders.append(obj.ipaddr)
                        rfcholderset = set(rfcholders)
                    print("RFC available with",rfcholderset)
                elif method=="LIST":
                    #LIST ALL P2P-CI/1.0
                    #Host: thishost.csc.ncsu.edu
                    #Port:
                    rfcs = []
                    for i in range(0,len(list_of_rfcs)):
                        obj = list_of_rfcs[i]
                        rfcs.append(obj.rfcno)
                        rfcset = set(rfcs)
                    print("RFC available with the server",rfcset)
                else:
                    pass


    def printPeerList(self):
        global list_of_peers
        for x in list_of_peers:
            print(x)
    
    def printRFCList(self):
        global list_of_rfcs
        for x in list_of_rfcs:
            print(x)

server = TCPServer()
while 1:
    connectionSocket, addr = server.serverSocket.accept()
    print("INCOMING CLIENT",addr)
    _thread.start_new_thread(server.threadPerClient, (connectionSocket,addr))
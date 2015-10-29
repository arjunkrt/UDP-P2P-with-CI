from socket import *
import Lists
import RFCLists
import _thread


list_of_peers = []
list_of_rfcs = []
class TCPServer(object):

    serverPort = 7734
    no_of_clients = 0;
    serverSocket = socket(AF_INET,SOCK_STREAM)

    serverSocket.bind(("192.168.1.9",serverPort))
    serverSocket.listen(10)
    print("The server is listening")
    def threadPerClient(self,peersocket,addr):
        
        
        global list_of_peers
        peer = Lists.LLNodePeer()
        peer.set_ipaddr(addr[0])
        peer.set_portno(int(addr[1]))
        #global RFCList
        list_of_peers.append(peer)

        print(len(list_of_peers))
        
        
        command = peersocket.recv(4096)
        decodedCom = command.decode()
        commandlines = decodedCom.split("|")
        firstline = commandlines[0]
        method = firstline.split()[0]
        global list_of_rfcs

        if method=="ADD":
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
            print(len(list_of_rfcs))
            
        elif method=="LOOKUP":
            self.processLookupRequest(peersocket,addr,commandlines)
        elif method=="LIST":
            self.processListRequest(peersocket,addr,commandlines)
        else:
            pass
        
        while 1:
            data = peersocket.recv(1024)
            if not data:
                break
            peersocket.send("REQUESTED RFC".encode())
        peersocket.close()
        
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
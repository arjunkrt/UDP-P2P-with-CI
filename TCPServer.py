from socket import *
from p1 import Lists
import _thread

serverPort = 7734
serverSocket = socket(AF_INET,SOCK_STREAM)

#In the line below give the local IP address of
#the machine if the clients and server are in the same network.
serverSocket.bind(("192.168.1.10",serverPort))
serverSocket.listen(1)
print("The server is listening")
#var = 0
peerList = None

#every separate client will be serviced by a separate thread
#The following function is called by different threads for different clients
def threadPerClient(peersocket):
    print("new thread spawned")
    peersocket.send("CONNECTION ESTABLISHED.ENTER REQUIRED RFC NO".encode())
    while 1:
        data = peersocket.recv(1024)
        if not data:
            break
        peersocket.send("REQUESTED RFC".encode())
    peersocket.close()

#function to print the server's list of peers
def printPeerList():
    if peerList is None:
        print("NO ACTIVE PEERS")
    else:
        current = peerList.head
        while current is not None:
            print("-->"),
            print(current.get_ipaddr(),current.get_portno(), sep=" "),
            current = current.get_next()
    return
#TCP central server's main thread starts here
while 1:
    connectionSocket, addr = serverSocket.accept()
    print("INCOMING CLIENT",addr)
    peer = Lists.LLNodePeer()
    peer.set_ipaddr(addr[0])
    peer.set_portno(addr[1])
    if peerList is None:
        peerList = Lists.LLPeer(peer)
    else:
        peerList.add(peer)
    #printPeerList()
    _thread.start_new_thread(threadPerClient, (connectionSocket,))
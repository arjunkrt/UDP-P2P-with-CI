#LLNodePeer is a node of the linked list that holds Peer information such as ip address and upload port
#LLPeer is the linked list of peers
class LLNodePeer(object):
    def __init__(self):
        self.ipaddr = None
        self.portno = None
        self.next_node = None

    def get_ipaddr(self):
        return self.ipaddr

    def set_ipaddr(self, ipaddr):
        self.ipaddr = ipaddr

    def get_portno(self):
        return self.portno

    def set_portno(self, portno):
        self.portno = portno

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

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


class LLPeer(LLNodePeer):
    def __init__(self, head=None):
        self.head = head

    def add(self, node):
        node.set_next(self.head)
        self.head = node

    def len(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def find(self, ipaddr):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == ipaddr:
                found = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        return current

    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

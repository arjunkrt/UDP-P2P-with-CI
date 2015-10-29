#LLNodeRFC is a node of the linked list that holds RFC information such as RFC name, RFC id and ip address
#LLRFC is the linked list of the list of above mentioned RFCs

class LLNodeRFC(object):
    def __init__(self):
        self.ipaddr = None
        self.rfcno = None
        self.rfcname = None
        self.next_node = None

    def xget_ipaddr(self):
        return self.ipaddr

    def xset_ipaddr(self, ipaddr):
        self.ipaddr = ipaddr

    def xget_rfcno(self):
        return self.rfcno

    def xset_rfcno(self, rfcno):
        self.rfcno = rfcno

    def xget_rfcname(self):
        return self.rfcname

    def xset_rfcname(self, rfcname):
        self.rfcname = rfcname

    def xget_next(self):
        self.next_node

    def xset_next(self, new_next):
        self.next_node = new_next

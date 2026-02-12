class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class Linklist:
    def __init__(self):
        self.head = None

    def add_values(self,data):
        if self.head is None:
            self.head=Node(data,self.head)
            return

        node=Node(data,self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("linked list is empty")
        itr=self.head
        llstr=''
        while itr:
            llstr+=str(itr.data) + '->'
            itr=itr.next

        print(llstr)

    def reverse(self):


ll=Linklist()
ll.add_values(3)
ll.add_values(4)
ll.print()


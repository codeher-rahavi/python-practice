class Node:
    def __init__(self,data=None,next=None,prev=None):
        self.data = data
        self.next=next
        self.prev=prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insertion(self,data):
        if self.head is None:
            self.head = Node(data,None,self.head)
            return

        itr=self.head
        while itr.next:
            itr = itr.next
        node=Node(data,None,itr)
        itr.next = node

    def print(self):
        if self.head is None:
            return "linked list is empty"

        itr= self.head
        dbll = ""
        while itr:
            dbll += str(itr.data) + "->"
            itr = itr.next

        print(dbll)

    def Forwardtraverrsal(self):
        if self.head is None:
            return "linked list is empty"
        itr=self.head
        while itr:
            print(itr.data," ")
            itr=itr.next

    def BackwardTraversal(self):
        if self.head is None:
            return "linked list is empty"

        itr=self.head
        while itr.next:
            itr=itr.next
        while itr.prev:
            print(itr.data," ")
            itr=itr.prev

    def deletion(self,value):
        if self.head is None:
            return "linked list is empty"
        itr=self.head
        while itr:
            if itr.data == value:

                if itr.prev == None:
                    self.head = itr.next
                    if self.head:
                        self.head.prev = None
                else:
                    itr.prev.next = itr.next
                    if itr.next:
                        itr.next.prev = itr.prev
                return
            itr=itr.next

    def insert_at_middle(self,index,value):
        if self.head is None:
            return "linked list is empty"

        count=0
        itr=self.head
        while itr:
            if count==index:
                node=Node(value,itr.next,itr.prev)
                itr.prev.next=node
                if itr.next:
                    itr.next.prev= node

            itr=itr.next



dll = DoublyLinkedList()
dll.insertion(3)
dll.insertion(4)
dll.insertion(8)
dll.insertion(23)
dll.insertion(18)
dll.insert_at_middle(1,45)

dll.deletion(4)
dll.print()
# dll.Forwardtraverrsal()
# dll.BackwardTraversal()





class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None

    def insert_at_begining(self,data):
        node=Node(data,self.head)
        self.head=node

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return

        itr=self.head
        while itr.next:
            itr=itr.next

        itr.next=Node(data,None)
    def print(self):
        if self.head is None:
            print("the linked list is empty!")

        s=''
        itr=self.head
        while itr:
            s += str(itr.data)
            itr=itr.next

        print(s)

    def array(self):
        a=''
        itr=self.head
        while itr:
            a+=str(itr.data)
            itr=itr.next


        a=int(a)*2
        a=list(str(a))
        a.reverse()
        self.head=None

        for i in a:
           self.insert_at_begining(int(i))



if __name__=='__main__':
    ll=LinkedList()
    ll.insert_at_end(1)
    ll.insert_at_end(8)
    ll.insert_at_end(9)
    ll.array()
    ll.print()
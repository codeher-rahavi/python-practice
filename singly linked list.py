class Node:
    def __init__(self, data=0, next=None):
        self.data=data
        self.next=next

class linkedlist:
    def __init__(self):
        self.head=None

    def insert_at_beginning(self,data):
        node=Node(data,self.head)
        self.head=node

    def print(self):
        if self.head is None:
            print("linked list is empty")
            return

        itr=self.head
        llstr=''
        while itr:
            llstr+= str(itr.data) + '-->'
            itr = itr.next

        print(llstr)

    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return

        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None)

    def insert_at(self,data):
        for i in data:
            self.insert_at_end(data)

    def reverse(self):
        prev = None
        current = self.head
        while current:
            nxt = current.next
            current.next=prev

            prev=current
            current=nxt
        self.head = prev





if __name__== '__main__':
    ll=linkedlist()
    ll.insert_at_beginning(34)
    ll.insert_at_beginning(12)
    ll.insert_at_end(2)
    ll.insert_at('1')
    ll.reverse()
    ll.print()
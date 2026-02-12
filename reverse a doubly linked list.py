class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None

    def insert(self,data):
        node=Node(data,self.head)
        self.head=node

    def print(self):
        if self.head is None:
            print("linked list is empty")
        itr=self.head
        llstr=''
        while itr:
            llstr += str(itr.data) + '->'
            itr=itr.next

        print(llstr)

    def reverse(self):
        prev = None
        curr = self.head

        while curr:
            next_node = curr.next  # store next
            curr.next = prev  # reverse link
            prev = curr  # move prev
            curr = next_node  # move curr

        self.head = prev





ll=LinkedList()
ll.insert(4)
ll.insert(5)
ll.insert(6)
ll.insert(7)
ll.insert(8)
ll.insert(9)
ll.reverse()
ll.print()



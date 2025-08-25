class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next= next

class linkedList:
    def __init__(self):
        self.head= None

    def add_at_beginning(self,data):
        node = Node(data,self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("the list is empty")

        itr=self.head
        llstr=''
        while itr:
            llstr += str(itr.data) + '->'
            itr=itr.next

        print(llstr)

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)

        itr=self.head
        while itr.next:
            itr=itr.next

        itr.next=Node(data,None)

    def insert_at_location(self,index,data):

        if index==0:
            self.add_at_beginning(data)

        if self.head is None:
            self.head = Node(data,Node)

        itr = self.head
        count=0
        while itr:
            if count == index-1:
                itr.next=Node(data,itr.next)

            itr=itr.next
            count+=1

    def length(self):
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next

        return count

    def delete_at_beginning(self):
        if self.length()==0:
            print("the list is empty")
            return
        if self.length()==1:
            print("removed the only one element")
            self.head=None
            return

        self.head=self.head.next



    def delete_at_end(self):
        if self.length() == 0:
            print("the list is empty")
            return
        if self.length() == 1:
            print("removed the only one element")
            self.head = None
            return

        itr=self.head
        while itr.next.next:
            itr=itr.next
        itr.next=None

    def delete_at_position(self,index):
        if self.head is None:
            print("the list is empty")

        count=0
        itr=self.head
        while itr:
            if count==index-1:
                itr.next=itr.next.next
            itr=itr.next
            count+=1



if __name__=='__main__':
    ll=linkedList()
    ll.add_at_beginning(23)
    ll.add_at_beginning(4)
    ll.add_at_beginning(3)
    ll.insert_at_end(1)
    ll.insert_at_location(0,40)
    ll.delete_at_beginning()
    ll.delete_at_end()
    ll.delete_at_position(2)
    ln=ll.length()
    print(ln)
    ll.print()

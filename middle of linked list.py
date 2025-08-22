class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next


class linkedList:
    def __init__(self):
        self.head=None

    def add_to_list(self,data):
        node = Node(data,self.head)
        self.head=node

    def print(self):
        if self.head is None:
            print("the linked list is empty")

        itr=self.head
        llstr=''
        while itr:
            llstr += str(itr.data) + '-->'
            itr=itr.next

        print(llstr)

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,self.head)
            return

        itr=self.head
        while itr.next:
            itr=itr.next

        itr.next= Node(data, None)

    def insert_values(self,data_list):
        for i in data_list:
            self.insert_at_end(i)


    def  length(self):
        count=0
        if self.head is None:
            print("the length of linked list is zero")

        itr=self.head
        while itr:
            count+=1
            itr=itr.next

        return count

    def print_middle(self,index):
        if self.head is None:
            print("the list is empty")
        if index<0 or index>=self.length():
            raise Exception("invalid syntax")
        count=0
        itr=self.head
        while itr and count< index:
            itr=itr.next
            count+=1

        middle=''
        while itr:
            middle += str(itr.data) + '-->'
            itr=itr.next

        print(middle)



if __name__ == '__main__':
    ll=linkedList()
    ll.insert_values([1,2,3,4,5,6])
    ll.print()
    l=ll.length()
    print(l)
    m=l//2
    print(m)
    ll.print_middle(m)
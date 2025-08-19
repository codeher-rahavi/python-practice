from logging import exception


class Node:
    def __init__(self, data=None,next=None):
        self.data=data
        self.next=next

class linkedlist:
    def __init__(self):
        self.head=None

    def insert_at_beginning(self,data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr=self.head
        llstr=''
        while itr:
            llstr += str(itr.data) + '-->'
            itr=itr.next

        print(llstr)

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return

        itr=self.head
        while itr.next:
            itr=itr.next

        itr.next = Node(data,None)

    def insert_values(self,data_list):
        for data in data_list:
            self.insert_at_end(data)

    def length(self):
        count=0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next

        return count

    def remove_at(self, index):
        if index<0 or index >=self.length():
            raise Exception("invalid index")
            return

        if index==0:
            self.head = self.head.next
            return
        count =0
        itr = self.head
        while itr:
            if count==index-1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count+=1


    def insert_at(self,index,data):
        if index<0 or index>self.length():
            raise Exception("invalid syntax")

        if index==0:
            self.insert_at_beginning(data)
            return

        count=0
        itr=self.head
        while itr:
            if count == index-1:
                node = Node(data, itr.next)
                itr.next=node
            itr = itr.next
            count+=1




if __name__ == '__main__':
    ll=linkedlist()
    ll.insert_at_beginning(35)
    ll.insert_at_beginning(8)
    ll.insert_at_end(7)
    ll.insert_values(['banana','apple','orange'])
    ll.remove_at(2)
    ll.insert_at(0,'figs')
    ll.print()
    ans=ll.length()
    print("length=",ans)

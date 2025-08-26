class Node:
    def __init__(self, data=None,next=None):
        self.data=data
        self.next=next

class linkedlist:
    def __init__(self):
        self.head=None

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return

        itr=self.head
        while itr.next:
            itr=itr.next

        itr.next = Node(data,None)

    def insert_values(self, data_list):
        for data in data_list:
            self.insert_at_end(data)

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr=self.head
        llstr=''
        while itr:
            llstr += str(itr.data)
            itr=itr.next

        #print(llstr)

        ans='0b'
        ans+=llstr
        print(int(ans,2))

if __name__=='__main__':
    ll=linkedlist()
    ll.insert_values([1,0,1])
    ll.print()
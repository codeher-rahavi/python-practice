class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class linkedList:
    def __init__(self):
        self.head=None

    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return

        itr=self.head
        while itr.next:
            itr=itr.next

        itr.next=Node(data,None)

    def insert_values(self,dataList):
        for i in dataList:
            self.insert_at_end(i)

    def print(self):
        if self.head is None:
            print("the list is empty")

        itr=self.head
        llstr=''
        while itr:
            llstr+=str(itr.data)
            itr=itr.next

        return llstr

    def order(self):
        val=[]
        itr=self.head
        while itr:
            val.append(itr.data)
            itr=itr.next

        val.sort()
        self.head=None
        self.insert_values(val)

if __name__=='__main__':
    ll=linkedList()
    ll.insert_values([4,1,2,3])
    ll.order()
    print(ll.print())
from wsgiref.validate import header_re


class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class linkedlist:
    def __init__(self):
        self.head = None

    def arr_to_linked_list(self,arr):
        if not arr:
            self.head=None
            return
        self.head = Node(arr[0])
        current=self.head
        for value in arr[1:]:
            current.next = Node(value)
            current = current.next


    def print(self):
        if self.head is None:
            print("linked list is empty")
            return None
        itr=self.head
        llstr=''
        while itr:
            llstr+= str(itr.data) + '-->'
            itr=itr.next

        print(llstr)

    def odd_even_list(self):
        if self.head is None:
            return

        odd=self.head
        even=self.head.next
        even_head=even

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next=odd.next
            even=even.next

        odd.next = even_head

if __name__=="__main__":
    ll=linkedlist()
    ll.arr_to_linked_list([1,2,3,4,5])
    print("original list")
    ll.print()
    ll.odd_even_list()
    print("after odd-even rearrangement")
    ll.print()
#output=[1,3,5,2,4] odd indices first and even indices next using singly linked list



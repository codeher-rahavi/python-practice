class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def insert_values(self, data_list):
        for data in data_list:
            self.insert_at_end(data)

    def length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self, index):
        if index < 0 or index >= self.length():
            raise Exception("Invalid index")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index > self.length():
            raise Exception("Invalid index")

        if index == 0:
            self.insert_at_beginning(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1


if __name__ == '__main__':
    ll = LinkedList()

    while True:
        print("\n--- Linked List Operations ---")
        print("1. Insert at beginning")
        print("2. Insert at end")
        print("3. Insert multiple values")
        print("4. Remove at index")
        print("5. Insert at index")
        print("6. Display linked list")
        print("7. Get length")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            data = input("Enter value to insert at beginning: ")
            ll.insert_at_beginning(data)

        elif choice == '2':
            data = input("Enter value to insert at end: ")
            ll.insert_at_end(data)

        elif choice == '3':
            data_list = input("Enter values separated by space: ").split()
            ll.insert_values(data_list)

        elif choice == '4':
            index = int(input("Enter index to remove: "))
            try:
                ll.remove_at(index)
            except Exception as e:
                print(e)

        elif choice == '5':
            index = int(input("Enter index to insert at: "))
            data = input("Enter value to insert: ")
            try:
                ll.insert_at(index, data)
            except Exception as e:
                print(e)

        elif choice == '6':
            ll.print()

        elif choice == '7':
            print("Length =", ll.length())

        elif choice == '8':
            print("Exiting...")
            break

        else:
            print("Invalid choice! Please try again.")

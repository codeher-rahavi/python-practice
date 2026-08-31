from collections import deque

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def build_tree(values):
    if not values or values[0] == -1:
        return None

    root = Node(values[0])

    queue = deque([root])
    i=1
    while queue and i<len(values):
        current = queue.popleft()

        #left Child
        if values[i] != -1:
            current.left = Node(values[i])
            queue.append(current.left)

        i+=1

        if i>=len(values):
            break

        #right child

        if values[i] !=-1:
            current.right = Node(values[i])
            queue.append(current.right)

        i+=1
    return root

def inorder(root):
    if root is None:
        return

    inorder(root.left)
    print(root.data , end=" ")
    inorder(root.right)

#standared input
values  = list(map(int,input().split()))
root = build_tree(values)
print("Inorder Travesal:")
inorder(root)

 
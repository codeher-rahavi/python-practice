from collections import deque

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def build_tree(num):
    if not num or num[0] == -1:
        return None

    root = Node(num[0])
    queue = deque([root])

    i=1

    while queue and i<len(num):
        curr = queue.popleft()

        if num[i] != -1:
            curr.left = Node(num[i])
            queue.append(curr.left)

        i+=1
        if i>=len(num):
            break

        if num[i] != -1:
            curr.right = Node(num[i])
            queue.append(curr.right)

        i+=1
        if i>=len(num):
            break

    return root




def search(root,key):
    if root is None:
        return None

    if root.data == key:
        return True

    return search(root.left,key) or search(root.right, key)

num = [12,3,5,1,6,7]
root = build_tree(num)
n=int(input("enter a number to search in the tree:"))
ans = search(root,n)
if ans :
    print("True")
else:
    print("False")
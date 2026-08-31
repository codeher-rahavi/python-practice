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

def Count_Nodes(root):
    if root is None:
        return 0
    else:
        return 1+Count_Nodes(root.left) + Count_Nodes(root.right)

nums=[12,23,45,7,9,4,6,3]
root = build_tree(nums)
print(Count_Nodes(root))

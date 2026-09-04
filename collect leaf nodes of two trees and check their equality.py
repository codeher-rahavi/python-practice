from collections import deque

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def build_tree(val):
    if not val:
        return None

    root = Node(val[0])
    queue = deque([root])
    i=1

    while queue and i< len(val) :
        curr  = queue.popleft()
        if val[i] != -1:
            curr.left = Node(val[i])
            queue.append(curr.left)

        i+=1
        if i>=len(val):
            break

        if val[i] != -1:
            curr.right  = Node(val[i])
            queue.append(curr.right)
        i+=1
        if i >=len(val):
            break

    return root

def leaf_Nodes(root1,root2):
    arr1 = []
    arr2 = []

    def tree1(root1):
        if root1 is None:
            return True
        if root1.left is None and root1.right is None:
            arr1.append(root1.data)
        else:
            tree1(root1.left)
            tree1(root1.right)
        return arr1

    a1 = tree1(root1)
    print(a1)

    def tree2(root2):
        if root2 is None:
            return True
        if root2.left is None and root2.right is None:
            arr2.append(root2.data)
        else:
            tree2(root2.left)
            tree2(root2.right)

        return arr2

    a2 = tree2(root2)
    print(a2)

    return a1 == a2


root1 = [3,5,1,6,2,9,8,-1,-1,7,4]
root2 = [3,5,1,6,7,4,2,-1,-1,-1,-1,-1,-1,9,8]
t1 = build_tree(root1)
t2 = build_tree(root2)
ans = leaf_Nodes(t1,t2)
print(ans)
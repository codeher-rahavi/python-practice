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

def depth(root):
    if root is None:
        return 0
    else:
        ans1 = depth(root.left)
        ans2 = depth(root.right)
        m = max( depth(root.left) , depth(root.right))

        return 1+m

values= [1,2,3,4,-1,5,6,-1,-1,7]
root = build_tree(values)
ans = depth(root)
print(ans)
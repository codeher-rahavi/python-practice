s="()))(("
c=0
stack=[]
for i in s:
    if i=="(":
        stack.append(")")
    else:
        if not stack or i!=stack.pop():
            c+=1

print(c)



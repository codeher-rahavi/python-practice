s = "((("
c=0
stack=[]
for i in s:
    if i =="(":
        stack.append(")")
    elif stack and stack.pop() == ")":
        continue
    else:
        c+=1

if c and len(stack)!=0:
     print(c+len(stack))
elif (c==0 and len(stack)!=0) or (c and len(stack)==0):
    print(c+len(stack))
else:
    print(0)
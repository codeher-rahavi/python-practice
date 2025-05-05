a=int(input("enter the array size:"))
array=[]
instruction=[]
for i in range(a):
    b=input("enter a command and two numbers:").split()
    command=b[0]

    if len(b)==3:
        num1,num2=int(b[1]),int(b[2])
        array.append([command,num1,num2])

    elif len(b)==2:
        num1=int(b[1])
        array.append([command,num1])

    else:
        array.append([command])

    instruction.append(command)

answer=[]
for i in array:
    if i[0] =="insert":
        answer.insert(i[1],i[2])
    if i[0]=="append":
        answer.append(i[1])
    if i[0]=="remove":
        answer.remove(i[1])
    if i[0]=="pop":
        answer.pop(i[1])

print(answer)


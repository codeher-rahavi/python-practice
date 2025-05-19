n=[5,5,10,10,20]
arr=[]
flag=1
if n[0]==5:
    arr.append(5)
else:
    flag=0

if flag==1:
    for i in range(1,len(n)):
        if n[i]==5:
            arr.append(5)
        elif n[i]==10:
            if 5 in arr:
                arr[arr.index(5)]=0
                arr.append(10)
            else:
                flag=0
                break
        elif n[i]==20:
            found=False
            for k in range(len(arr)):
                for l in range(len(arr)):
                    if k!=l and arr[k]+arr[l]==15:
                        arr[k]=0
                        arr[l]=0
                        arr.append(20)
                        found=True
                        break
                if found:
                    break
            if not found:
                flag=0
                break




if flag==0:
    print("no change")
else:
    print("yes change")




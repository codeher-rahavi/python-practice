nums=[1,0]
k=2
flag=0
for i in range(0,len(nums)):
    for j in range(0,len(nums)+1):
        if len(nums[i:j])>0:
            add=sum(nums[i:j])
            if add>0:
                if add%k==0:
                    flag=1



if flag==1:
    print("True")
else:
    print("False")





nums=[1,2,3,4]
elecount=0
digicount=0
for i in range(0,len(nums)):
    elecount+=nums[i]

rem=0
for i in range(0,len(nums)):
    while nums[i]!=0:
        rem=nums[i]%10
        digicount+=rem
        nums[i]//=10

res=elecount - digicount
if res<0:
    res= -(res)

print(res)



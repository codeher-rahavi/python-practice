nums = [2, 2, 1, 1, 1, 2, 2]
freq={}
count=len(nums)//2

for i in nums:
    if i not in freq:
        freq[i]=1
    else:
        freq[i]+=1

for i in freq:
    if freq[i]>count:
        print(i)

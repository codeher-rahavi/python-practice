'''dynamic programming'''
coins = [1,2,5]
amount = 11
arr = [float("inf")] * (amount+1)
arr[0]=0

for i in range(1,amount+1):
    for coin in coins:
        if coin<=i:
            arr[i]=min(arr[i],arr[i-coin]+1)

ans=arr[amount] if arr[amount]!=float('inf') else -1
print(ans)







a = [0, 1, 0, 3, 2, 3]
dp=[1]*len(a)
for i in range(len(a)):
    for j in range(i):
        if a[i]>a[j]:
            dp[i]=max(dp[i],dp[j]+1)

print(max(dp))



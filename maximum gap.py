a=[1,3,6,2,9]
if len(a)<2:
    print("not enough elements")
else:
    a.sort()
    max_diff=0
    for i in range(1,len(a)):
        if max_diff < a[i]-a[i-1]:
            max_diff= a[i] -a[i-1]

print(max_diff)
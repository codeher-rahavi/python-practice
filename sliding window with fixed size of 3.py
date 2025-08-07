s = "abab"
p = "ab"
arr=[]
end=(len(s)-len(p))+1
inc=len(p)
com=sorted(p)
for i in range(end):
    if sorted(s[i:i+inc])==com:
        arr.append(i)

print(arr)
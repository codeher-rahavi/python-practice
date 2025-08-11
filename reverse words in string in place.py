s="Let's take leetcode contest"
s=list(s)
print(s)
start=0
for i in range(0,len(s)):
    if s[i]==' ':
        end=i-1
        while start<end:
            s[start],s[end]=s[end],s[start]
            start+=1
            end-=1
        start=i+1

end=i
while start<end:
    s[start],s[end]=s[end],s[start]
    start+=1
    end-=1
s=''.join(s)
print(s)
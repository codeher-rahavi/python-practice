a=["h","e","l","l","o"]
l=0
r=len(a)-1
while l<r:
    a[l],a[r]=a[r],a[l]
    l+=1
    r-=1

print(a)


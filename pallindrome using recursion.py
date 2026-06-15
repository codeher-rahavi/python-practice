def pallindrome(n,start,end):
    if start >= end :
        return True
    elif n[start] != n[end]:
        return False
    else:
        return pallindrome(n,start+1,end-1)

a = input()
b=''
ans = pallindrome(a,0,len(a)-1)
print(ans)
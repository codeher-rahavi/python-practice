s="pwwkew"
a=s
if len(set(s)) == 1:
    print(1)
else:
    i=0
    j=0
    m=0
    seen=set()
    while j<len(s):
        if s[j] not in seen:
            seen.add(s[j])
            m=max(m,j-i+1)
            j+=1
        else:
            seen.remove(s[i])
            i+=1

    print(m)



'''use sliding window'''






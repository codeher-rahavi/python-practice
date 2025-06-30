def stringrotate(a,g):
    if len(a)!=len(g):
        return False
    c=a+a
    if g in c:
        return True
    else:
        return False

print(stringrotate("abcde","deabc"))
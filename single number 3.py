def singlenum(n):
    seen=set()
    for i in n:
        if i not in seen:
            seen.add(i)
        else:
            seen.remove(i)

    return list(seen)

print(singlenum([1,2,1,2,3,5]))


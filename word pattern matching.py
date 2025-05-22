pattern="abba"
s="dog cat cat dog"

arr=s.split()
arr2=list(pattern)

if len(arr)!=len(arr2):
    print("False")
else:
    map1={}
    map2={}
    flag=1
    for i in range(len(arr)):
        word=arr[i]
        char=arr2[i]
        if word not in map1 and char not in map2:
            map1[word]=char
            map2[char]=word
        elif map1.get(word)!=char or map2.get(char)!=word:
            flag=0
            break

    if flag==1:
        print("True")
    else:
        print("False")


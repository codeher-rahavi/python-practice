def vowel(string):
    v_count=0
    c_count=0
    l=len(string)
    for i in range(l):
        if string[i] in ['a','e','i','o','u']:
            v_count +=1
        elif string[i] not in ['a','e','i','o','u'] and string[i]!=' ':
            c_count+=1

    return v_count,c_count


str=input()
vow,const = vowel(str)
print("vowel = ",vow,"consonant= ",const)
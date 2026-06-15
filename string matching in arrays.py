words =["leetcoder","leetcode","od","hamlet","am"]
arr=[]
for i in range(len(words)):
    for j in range(len(words)):
        if words[j] in words[i] and words[i]!=words[j]:
            arr.append(words[j])

print(list(set(arr)))
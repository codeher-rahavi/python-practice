sentence = "i love eating burger"
searchWord = "burg"
l=len(searchWord)
arr=sentence.split(" ")
for i in range(len(arr)):
    if searchWord in arr[i] and searchWord[0:l] == arr[i][0:l]:
        print(i+1)




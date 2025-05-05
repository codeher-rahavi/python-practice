a=input("enter a string:")
b=input("enter a word to search:")
index_found=a.find(b)
if index_found!=-1:
    print(index_found)
else:
    print("-1")
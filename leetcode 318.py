words = ["abcw","baz","foo","bar","xtfn","abcdef"]
s = []
for i in words:
    s.append("".join(sorted(i)))

print(s)



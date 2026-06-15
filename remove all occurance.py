s = "a"
part = "aa"
l=len(part)
while True:
    i = s.find(part)
    s=s[0:i] + s[i+l:]
    if part not in s:
        break

print(s)



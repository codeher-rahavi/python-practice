import hashlib

text = "hello"
hash_val = hashlib.sha256(text.encode()).hexdigest()
print(hash_val)

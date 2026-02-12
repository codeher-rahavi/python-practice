PRIVATE_KEY = 'secret'
PUBLIC_KEY = 'secret'

def hash_file(text):
    hash_value=0
    for i ,j in enumerate(text):
        hash_value+=(i+1)* ord(j)
    return hash_value %100000


def get_signature(document):
    content= document+PRIVATE_KEY
    signature=hash_file(content)

    return signature

def verify_signature(document,signature):
    content = document+PUBLIC_KEY
    verify_signature = hash_file(content)

    return signature == verify_signature

def main():
    doc= input("enter the original text ")

    signature = get_signature(doc)
    print(" Generated signature=",signature)

    if(verify_signature(doc,signature)):
        print("corrected signature")
    else:
        print("Incorrect signature ")

    tampered= input("enter a tampered text")
    if(verify_signature(tampered,signature)):
        print("correct tampered text")
    else:
        print("tampered text")

if __name__=="__main__":
    main()

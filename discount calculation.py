a=int(input())
dis=0
if a <=0:
    print("Invalid input")
elif a<=500 and a>0:
    dis=a*0.05
elif a>500 and a<=1000:
    dis=a*0.1
elif a>1000 and a <=2000:
    dis=a*0.15
if(dis>0):
    print(dis)
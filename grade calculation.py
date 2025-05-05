m1,m2,m3,m4,m5,m6= map(float,input().split())
if any(m<0 or m>100 for m in [m1,m2,m3,m4,m5,m6]):
    print("Invalid marks")
else:
   total=(m1+m2+m3+m4+m5+m6)/6
   res='{:.2f}'.format(total).rstrip('0').rstrip('.')
   if total>=95:
       print(f"{res} A")
   elif total >= 85:
       print(f"{res} B")
   elif total >= 75:
       print(f"{res} C")
   elif total >= 65:
       print(f"{res} D")
   elif total >= 45:
       print(f"{res} E")
   elif total < 45:
       print(f"{res} F")

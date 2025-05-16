'''understanding git and github'''
hr,mins=map(int,input().split(':'))
if hr==00 and mins==00:
    print("12:00 AM")
elif hr==12 and mins==00:
    print("12:00 PM")
elif hr>12:
    print(f"{hr-12}:{mins:02d} PM")
elif hr<12 :
    print(f"{hr} : {mins:02d} AM")


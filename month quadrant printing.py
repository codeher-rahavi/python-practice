month=int(input())
first=[1,2,3]
sec=[4,5,6]
third=[7,8,9]
four=[10,11,12]
qua=0
days=0
days_31=[1,3,5,7,8,10,12]
days_30=[2,4,6,9,11]
if month<=0 or  month>13:
    print("Invalid month entered")
else:
    if month in days_31:
        days="31 days"
        if month in first:
            qua="First Quandrant"
        if month in sec:
            qua="second Quandrant"
        if month in third:
            qua="third Quandrant"
        if month in four:
            qua="Fourth Quandrant"

    if month in days_30:
        days="30 days"
        if month in first:
            qua = "First Quandrant"
        if month in sec:
            qua = "second Quandrant"
        if month in third:
            qua = "third Quandrant"
        if month in four:
            qua = "Fourth Quandrant"

    print(f"{days},{qua}")
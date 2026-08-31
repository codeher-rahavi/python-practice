def calculate_grade(marks):
    total_marks = sum(marks)
    average = sum(marks) / len(marks)
    grade=0
    if average >=90:
        grade = 'A'
    elif average >=75:
        grade='B'
    elif average >=50:
        grade = 'C'
    else:
        average = 'Fail'

    return total_marks,average,grade

n=int(input())
arr=[]
for i in range(n):
    b=int(input())
    arr.append(b)

ans = calculate_grade(arr)
print(ans)


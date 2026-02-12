def selection_sort(nums):
    l=len(nums)
    for i in range(l):
        m=i
        for j in range(i+1,l):
            if nums[j][1] > nums[m][1] or (nums[j][1]==nums[m][1] and nums[j][0] < nums[m][0]):
                m=j
        nums[i],nums[m]=nums[m],nums[i]
def main():
    n=int(input("enter the number of students:"))
    students=[]
    for i in range(n):
        name=input("enter your name:")
        grade = int(input("enter your grade:"))
        students.append((name,grade))

    selection_sort(students)

    print("sorted list of students")
    for i ,j in students:
        print(f"{i}:{j}")


if __name__ == "__main__":
    main()
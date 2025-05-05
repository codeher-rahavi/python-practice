pen1=input("pen:")
note1=input("notebook:")
pencil1=input("pencil:")
try:
    pen=int(pen1)
    note=int(note1)
    pencil=int(pencil1)
    if pen<=0 or note<=0 or pencil<=0:
        print("Invalid")
    else:
        print("Total:",pen*20+note*70+pencil*9)
except ValueError:
    print("Invalid")




rows=int(input("Please enter the number of rows: "))

for i in range(1, rows + 1):
    print(" "* (rows-i),end=" ") #spaces
    for j in range(1,2*i):
        print(j, end="")#numbers
    print()


for i in range(rows - 1, 0, -1):
    print(" "* (rows-i),end=" ") #spaces
    for j in range(1,2*i):
        print(j, end="")#numbers
    print()
print("Half Pyramid Pattern of dollar sign! ($)")
n=int(input("Please enter in the number of rows "))
for i in range(n):
    for j in range(i+1):
        print("$ ", end="")
print()
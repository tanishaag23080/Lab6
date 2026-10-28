n = int(input("Enter an odd positive integers: "))

for i in range(n//2):
    for j in range((n//2)-i):
        print(" ",end="")

    for j in range(2*i+1):
        print("*",end="")

    print()

for i in range(n//2,-1,-1):
    for j in range(n//2-i):
        print(" ",end="")
    for j in range(2*i+1):
        print("*",end="")
    print()

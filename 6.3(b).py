n=int(input("Enter a number"))
i=n
while i>0:
    j=1  #j means column
    while j<=i:
        print("*","\t",end="")
        j+=1
    print()
    i-=1

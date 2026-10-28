n=int(input("Enter number"))
i=1
while i<=1000:
    x=i%n
    y=i%4
    if x==0 and y!=0:
        print(i,"\t",end="")
    i+=1
        
        

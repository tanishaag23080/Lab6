n=int(input("Enter a number"))
count=0
for i in range(1,1001):
    x=i%n
    y=i%4
    if x==0 and y!=0:
        print(i,"\t",end="")
        
        

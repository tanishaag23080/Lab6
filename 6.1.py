print( " Addition Table " )
for i in range (1,10):
    print("\t",i,end="")
print()
print(" ","_"*35)
for i in range (1,10):
    print(i,"|\t",end="")
    for j in range (1,10):
        print(i+j,"\t",end="")
    print()
        

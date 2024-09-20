pattern = int (input("Enter the size of the pattern:"))
i=0
while i<pattern:
    j=0
    for j in range (pattern):
        print("*", end="") 
        j=j+1 
    print()
    i=i+1    

rows=int(input("enter no. of rows"))

current = 1
for row in range(1,rows):
    for col in range(1,row+1):
        
        print(current, end=' ')
        current += 1
    print("")
 

list1=[12,23,11,'item','abc',45,'rrr']
length=len(list1)
list2=[]
list3=[]
i=0
sq=0
while(i<length):   
    if(list1[i] is int):
        
        sq=list1[i]*list1[i]
        list2.append(sq)
    else:
        list3.append(list1[i])
    i+=1    
print(list2)
print(list3)

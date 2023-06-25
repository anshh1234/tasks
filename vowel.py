string=input("give string")
vow='a','e','i','o','u','A','E','I','O','U'
count=0
a=0
e=0
o=0
i=0
u=0
A=0
E=0
O=0
I=0
U=0
        

for ch in string:
    if(ch in vow):
        count+=1
        
        for v in ch:
            
            if(v=='a'):
                a+=1
            elif(v=='e'):
                e+=1
            elif(v=='i'):
                i+=1
            elif(v=='o'):
                o+=1
            elif(v=='u'):
                u+=1
            elif(v=='A'):
                A+=1
            elif(v=='E'):
                E+=1
            elif(v=='I'):
                I+=1
            elif(v=='O'):
                O+=1
            elif(v=='U'):
                U+=1
                
print("no. of vowel in input string is:",count,a,e,i,o,u,A,E,I,O,U)        

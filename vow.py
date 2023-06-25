string=input("give string")
vow='a','e','i','o','u','A','E','I','O','U'
count=0
newstr=string
for ch in string:
    if(ch in vow):
        count+=1
        newstr=newstr.replace(ch,"#")
print("no. of vowel in input string is:",count)
print("new string with vowels being replaced by # is:",newstr)

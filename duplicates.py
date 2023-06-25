string=input("enter sentence")
words=string.split()
word_dict={}

for word in words:
    if(word in word_dict):
        word_dict[word]+=1
    else:
        word_dict[word]=1

for key,value in word_dict.items():
    if(value>1):
        print(key)
    else:
        print(key)
        
        

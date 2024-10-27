word=input("please enter any word : ")
charac=input("please enter any character from the word : ")
i=0
count=0
while (i<len(word)):
    if (word[i]==charac) :
        count=count+1
    i=i+1

print("number of times ",charac," has occured : ",count)
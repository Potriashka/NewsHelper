# Key Word(s) - KW

# creating an empty list
KeyWords = []
 
# number of KW in input
KWnum = int(input("Enter number of key words : "))
 
# iterating till the range
for i in range(0, KWnum):
    ele = input()
 
    KeyWords.append(ele) # adding the KW
     
print(KeyWords)
KeyWords = str(KeyWords)
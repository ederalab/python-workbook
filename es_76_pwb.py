#is string palindrome?
word = input("Insert the string and check if is a palindrome: ")
alphabet = "abcdefghijklmnopqrstuvwxyz"
count = len(word)
wordwo = ""
i = 0
while i < count:
    if word[i] in alphabet:
        wordwo = wordwo + word[i]
    i +=1

count = len(wordwo)

i = 0
n = count -1

pal = True

while i < count:
    if wordwo[i] != wordwo[n]:
        pal = False
    i += 1
    n -= 1

if pal:
    print ("The string",word,"is palindrome")
else:
    print ("The string",word,"is not palindrome")

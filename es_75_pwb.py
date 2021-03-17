#is string palindrome?
word = input("Insert the word and check if is a palindrome: ")
count = len(word)
i = 0
n = count -1
pal = True

while i < count:
    if word[i] != word[n]:
        pal = False
    i += 1
    n -= 1

if pal:
    print ("The word",word,"is palindrome")
else:
    print ("The word",word,"is not palindrome")
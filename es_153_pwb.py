# Find the Longest Word in a File

import os

dir_path = os.path.dirname(os.path.realpath(__file__))
filename = dir_path + '/file_utili/elements.txt'

longest_words = []
myfile = open(filename, 'r')

for l in myfile:
    line = myfile.read()

    for word in line.split():
        if len(longest_words) == 0:
            longest_words.append(word)

        longest = max(longest_words, key=len)

        if len(word) >= len(longest):
            if len(word) != len(longest):
                del longest_words[:]
            longest_words.append(word)

myfile.close()

print(longest_words)
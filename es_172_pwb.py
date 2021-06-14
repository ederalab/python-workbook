# Word with 6 vowels in order

import os

dir_path = os.path.dirname(os.path.realpath(__file__)) + '/file_utili/'
filename = dir_path + 'words.txt'


def check_word(filename):
    vowels = "AEIOUY"
    words = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            for word in line.split():
                words.append(word)

    for word in words:
        i = 0
        check = ""
        for c in word:
            if c.upper() in vowels and c.upper() == vowels[i]:
                i += 1
                check += c.upper()
            elif c.upper() in vowels and c.upper() != vowels[i]:
                check = ""

            if vowels == check:
                print(word)

check_word(filename)
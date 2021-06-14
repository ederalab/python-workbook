# A book with no E...

import os
from es_154_pwb import letters

def check_letters(filename):
    letters_in_file = letters()
    with open(filename) as f:
        for line in f:
            line = line.rstrip()
            for word in line.split():
                word = word.lower()
                word = word.replace(",", "").replace(".", "").replace(" ", "").replace("'", "").replace('"',"").replace("?","").replace("!", "").replace(";", "").replace(":", "")

                for l in word:
                    if l in letters_in_file:
                        letters_in_file[l] += 1

    return letters_in_file


def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    filename = dir_path + '/file_utili/emma.txt'

    try:
        myfile = open(filename, 'r')
        result = check_letters(filename)
        letters_in_file = sorted(result.items(), key=lambda x: x[1], reverse= True)
        print('Recurrence of each letter in the file')
        for k,v in letters_in_file:
            print(k.upper(), v)
        myfile.close()
    except:
        print('An error occurred while reading the file!')


if __name__ == '__main__':
    main()
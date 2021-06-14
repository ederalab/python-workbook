# Number the Lines in a File

import os

dir_path = os.path.dirname(os.path.realpath(__file__))
filename = dir_path + '/file_utili/words.txt'

def read_file(filename):
    myfile = open(filename, 'r')
    limit = len(myfile.readlines())
    myfile.close()

    myfile = open(filename, 'r')

    new_file_content = []

    for i in range(limit) :
        line = myfile.readline()
        new_file_content.append(str(i) + ', '+ line)

    myfile.close()
    return new_file_content


def write_file(l):
    newfilename = dir_path + '/file_utili/new_from_words.txt'
    mynewfile = open(newfilename, 'w')

    for line in l:
        mynewfile.write(line + '\n')

    mynewfile.close()
    print("Done!")


# read_file(filename)
write_file(read_file(filename))






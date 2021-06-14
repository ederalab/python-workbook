# Consistent Line Lengths
import os


def line_length(filename, lenght):
    newfile = ""
    count = 0
    try:
        with open(filename, 'r') as myfile:
            for line in myfile.readlines():
                if line != '\n':
                    for words in line.split():
                        if count <= (lenght - len(words)):
                            newfile += words + ' '
                            count += len(words) + 1
                        else:
                            newfile += '\n'
                            count = 0
                else:
                    newfile += '\n\n'
                    count = 0
    except:
        print('Error while reading the file', filename)


    try:
        newfilename = filename[:-4] + '_mod' + filename[-4:]
        with open(newfilename, 'w') as myfile:
            myfile.write(newfile)
    except:
        print('Error while writing the new file', newfilename)

    return True



def main():
    dir_path = os.path.dirname(os.path.realpath(__file__)) + '/file_utili/'
    #filename = dir_path + 'alice_in_wonderland.txt'
    #lenght = 50

    filename_user = input('Insert the name of the file: ')
    filename = dir_path + filename_user
    lenght = int(input('Insert the lenght of the parameter: '))
    result = line_length(filename, lenght)

    if result:
        print('Done, check the new file!')


if __name__ == '__main__':
    main()



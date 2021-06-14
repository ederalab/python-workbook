# Spell Checker

from es_117_pwb import onlyWords
import sys, os


def spell_checker(word_list, filename):
    result = []
    word_dict = dict()
    try:
        myfile = open(word_list, 'r')
        for line in myfile.readlines():
            add_line = line.split()
            word_dict[add_line[0].lower()] = 0
        myfile.close()
    except:
        print("Error in reading the word list")

    myfile = open(filename, 'r')
    for line in myfile.readlines():
        line = line.rstrip()
        line2check = line.split()
        for i in line2check:
            word = onlyWords(i)
            if not word[0].lower() in word_dict.keys():
                result.append(word[0].lower())
    myfile.close()
    return result


def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    if len(sys.argv) < 2:
        print('Provide minimum 2 file names as command line arguments')
        quit()

    word_list = dir_path + '/file_utili/words.txt'
    #filename = dir_path + '/file_utili/emma.txt'

    filename = dir_path + '/file_utili/' + sys.argv[1]

    #print(sys.argv[1], filename)

    result =  spell_checker(word_list, filename)

    if len(result) == 0:
        print('there are no mispelled words')
    else:
        print('here are the mispelled words: ')
        for word in result:
            print(word)


if __name__ == '__main__':
    main()

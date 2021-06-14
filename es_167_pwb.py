# Spell Checker

from es_117_pwb import onlyWords
import sys, os


def spell_checker(word_list, filename):
    result = []
    word_dict = dict()
    try:
        myfile = open(word_list, 'r')
        for line in myfile:
            add_line = line.strip()
            word_dict[add_line.lower()] = 0
        myfile.close()
    except:
        print("Error in reading the word list")

    myfile = open(filename, 'r')
    for line in myfile:
        for word in onlyWords(line):
            if word.lower() not in word_dict and not word.isdigit():
                if word.lower() not in result:
                    result.append(word.lower())
    myfile.close()
    return result


def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))

    if len(sys.argv) < 2:
        print('Provide minimum 2 file names as command line arguments')
        quit()

    word_list = dir_path + '/file_utili/words.txt'
    # filename = dir_path + '/file_utili/emma.txt'
    filename = dir_path + '/file_utili/' + sys.argv[1]

    result =  spell_checker(word_list, filename)

    if len(result) == 0:
        print('there are no mispelled words')
    else:
        print('here are the mispelled words: ')
        for word in result:
            print(word)


if __name__ == '__main__':
    main()

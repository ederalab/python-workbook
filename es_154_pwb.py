# Letter Frequencies

import os

def letters():
    all_letters = dict()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for l in alphabet:
        all_letters[l] = 0
    return all_letters


def letter_frequencies(myfile, all_letters):
    for l in myfile.read():
        if l.lower() in all_letters:
            all_letters[l.lower()] += 1

    return (all_letters)


def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    user_input = input('Please write the name of the file (with extension): ')
    #user_input = 'elements.txt'
    filename = dir_path + '/file_utili/' + user_input

    try:
        myfile = open(filename, 'r')
        result = letter_frequencies(myfile, letters())
        print('Here is the letters frequency of the file:\n')
        print(result)
        myfile.close()
    except:
        print("The name of the file wasn't correct, try again!")
        main()



if __name__ == '__main__':
    main()
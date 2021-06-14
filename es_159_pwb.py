# Two word random password
import os
import random


def generate_password(words):
    count = 0
    password = ''
    while True:
        word = random.choice(words)
        if len(word) >= 3 and count < 2:
            password += word.capitalize()
            count += 1
        elif count == 2 and 8 >= len(password) <= 10:
            break
        else:
            password = ''
            count = 0

    return password


def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    filename = dir_path + '/file_utili/words.txt'

    try:
        myfile = open(filename, 'r')
        with open(filename) as f:
            words = [line.rstrip() for line in f]
        password = generate_password(words)
        print('The random password is:', password)
        myfile.close()
    except:
        print('An error occurred while reading the file!')


if __name__ == '__main__':
    main()

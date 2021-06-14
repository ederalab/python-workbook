# What's the element again?

import os

def store_elements(filename):
    elements = dict()

    with open(filename) as f:
        for line in f:
            line = line.rstrip()
            split_elements = line.split(',')
            elements[split_elements[0]] = [split_elements[1], split_elements[2]]

    return elements


def check_elements(user_input, elements):
    user_input = str(user_input)
    if user_input in elements.keys():
        return True, elements[user_input]
    else:
        for key, value in elements.items():
            if user_input in value:
                return True, key

    return False, ''


def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    filename = dir_path + '/file_utili/elements.txt'

    try:
        myfile = open(filename, 'r')
        elements = store_elements(filename)
        while True:
            user_input = input('Enter the protons or the name or the symbol of an element: ')
            result, el = check_elements(user_input.capitalize(), elements)

            if result == True:
                if type(el) is list:
                    print(user_input, 'corresponds to the element', el[1], 'with symbol', el[0])
                else:
                    print(user_input, 'have protons', el)
                break
            else:
                print('There was an error in your input, try again!')

        myfile.close()
    except:
        print('An error occurred while reading the file!')


if __name__ == '__main__':
    main()
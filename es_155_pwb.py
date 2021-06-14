# Words that occur most

import os

def onlyWords(s):
    s = s.replace(",", " ").replace(".", " ").replace(":", " ").replace(";", " ").replace("?", " ").replace("!", " ").replace(" '", " ").replace("' ", " ").replace('"', " ").replace('\n', " ").replace('(', " ").replace(')', " ").replace('--', " ").replace('[', " ").replace(']', " ")
    t = s.split()
    return t


def word_frequencies(myfile):
    wf = dict()
    for line in myfile.readlines():
        words = onlyWords(line)
        for word in words:
            if word in wf:
                wf[word] += 1
            else:
                wf[word] = 1

    return wf


def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    user_input = input('Please write the name of the file (with extension): ')
    #user_input = 'emma.txt'
    filename = dir_path + '/file_utili/' + user_input
    try:
        myfile = open(filename, 'r')
        result = word_frequencies(myfile)
        sorted_result = sorted(result.items(), key=lambda x: x[1], reverse=True)
        num_of_words = 20

        print(f'The {num_of_words} most occurring words are:')

        for i in range(0, num_of_words):
            print(f'• "{sorted_result[i][0]}" occurring {sorted_result[i][1]} times')

        myfile.close()
    except:
        print("The name of the file wasn't correct, try again!")
        main()


if __name__ == '__main__':
    main()
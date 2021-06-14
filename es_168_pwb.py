# Repeated Words

import sys, os

def onlyWords(s):
    s = s.replace(",", " ").replace(".", " ").replace(":", " ").replace(";", " ").replace("?", " ").replace("!", " ").replace(" '", " ").replace("' ", " ").replace('"', " ")
    return s


def repeatedWords(filename):
    try:
        myfile = open(filename, 'r')
        count = 1
        check = []
        result = dict()
        for line in myfile.readlines():
            line = line.rstrip()
            for word in line.split():
                word = onlyWords(word.lower())

                if word in check:
                    result[word] = count
                else:
                    check.append(word)
            count += 1

        return result
        myfile.close()
    except:
        print('Error while opening the file!')


def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))

    if len(sys.argv) < 2:
        print('Provide minimum 2 file names as command line arguments')
        quit()

    #filename = dir_path + '/file_utili/parole.txt'
    filename = dir_path + '/file_utili/' + sys.argv[1]

    check = repeatedWords(filename)

    if bool(check) == False:
        print('There are no repeated words')
    else:
        print('There are repeated words: ')
        for w,l in check.items():
            print(w,l)



if __name__ == '__main__':
    main()

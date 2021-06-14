# Redacting Text in a File

import os

def onlyWords(s):
    s = s.replace(",", "").replace(".", "").replace(":", "").replace(";", "").replace("?", "").replace("!", "").replace(" '", "").replace("' ", "").replace('"', "")
    return s

def redact_text(filename, sensitive_words, new_filename):
    try:
        sw = dict()
        myfile = open(sensitive_words, 'r')
        for line in myfile.readlines():
            line = line.rstrip()
            for word in line.split():
                sw[word] = 0
        myfile.close()
    except:
        print('Error while opening the file!')
        quit()

    try:
        myfile = open(filename, 'r')
        newfile = open(new_filename, "w")

        line = myfile.readline()
        while line != "":
            line = line.rstrip()
            for word in sorted(sw, key=str.lower):
                count = len(word)
                line = line.replace(onlyWords(word), '*' * count)
            newfile.write(line)
            line = myfile.readline()

        newfile.close()
        myfile.close()
        return True
    except:
        print('Error while opening the file!')



def main():
    dir_path = os.path.dirname(os.path.realpath(__file__)) + '/file_utili/'
    filename = dir_path + 'original_169.txt'
    #sensitive_words = 'sensitive_words.txt'
    #new_filename = 'redacted_169.txt'
    sensitive_words_input = input('Insert the name of the sensitive words file: ')
    new_filename_input = input('Insert the name of the redicted file: ')
    sensitive_words = dir_path + sensitive_words_input
    new_filename = dir_path + new_filename_input

    result = redact_text(filename, sensitive_words, new_filename)
    if result == True:
        print("Done, check the file!")


if __name__ == '__main__':
    main()
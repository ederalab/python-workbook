# Weird Words
# I before E except after C
# believe, chief, fierce, friend // ceiling, receipt
import os


def check_words(words):
    respect_rule = []
    not_respect_rule = []

    for word in words:
        if 'cei' in word or 'ie' in word:
            respect_rule.append(word)
        else:
            not_respect_rule.append(word)

    return respect_rule, not_respect_rule


def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    filename = dir_path + '/file_utili/emma.txt'

    try:
        myfile = open(filename, 'r')
        words_to_check = []
        with open(filename) as f:
            for line in f:
                for word in line.split():
                    word = word.lower()
                    word = word.replace(",", "").replace(".", "").replace(" ", "").replace("'", "").replace('"', "").replace("?", "").replace("!", "").replace(";", "").replace(":", "")
                    if ('ie' in word or 'ei' in word) and word not in words_to_check:
                        words_to_check.append(word)

        respect_rule, not_respect_rule = check_words(words_to_check)

        print(f'Checking a list of {len(words_to_check)} words:\n{len(respect_rule)} respect the rule "I before E except after C" while {len(not_respect_rule)} are not.')
        print('\n')
        print('Check them all:')
        print('*** First group of words ***')
        for word in respect_rule:
            print(word, end=' / ')

        print('\n')
        print('\n*** Second group of words ***')
        for word in not_respect_rule:
            print(word, end=' / ')

        myfile.close()
    except:
        print('An error occurred while reading the file!')


if __name__ == '__main__':
    main()

# Distinct Names

import os

def walk(dirname):
    temp_girls = []
    temp_boys = []

    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)
        if os.path.isfile(path):
            if 'Girls' in path:
                temp_file = temp_girls
            else:
                temp_file = temp_boys

            try:
                myfile = open(path, 'r')
                for line in myfile.readlines():
                    temp = line.split()
                    if temp[0] not in temp_file:
                        temp_file.append(temp[0])
                myfile.close()
            except:
                print('Error while reading the directory: make sure you wrote a correct year name, try again.')
                quit()

    return temp_girls, temp_boys


def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    dirname = dir_path + '/file_utili/BabyNames/'
    girls, boys = walk(dirname)
    print('Here the list of every distinct names for boys and girls from 1900 to 2012!')
    count = 1
    print('\n*** GIRLS ***')
    print(f'({len(girls)} names)')

    for girl in sorted(girls):
        if count != len(girls):
            print(girl, end = ' - ')
        else:
            print(girl, end = '\n')
        count += 1

    count = 1
    print('\n*** BOYS ***')
    print(f'({len(boys)} names)')
    for boy in sorted(boys):
        if count != len(boys):
            print(boy, end = ' - ')
        else:
            print(boy, end = '\n')
        count += 1


if __name__ == '__main__':
    main()
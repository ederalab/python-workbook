# Most Births in a given Time Period

import os

def walk(dirname, first_year, last_year):
    temp_dict_girls = dict()
    temp_dict_boys = dict()
    year = first_year

    girls_file = '_GirlsNames.txt'
    boys_file = '_BoysNames.txt'

    while year <= last_year:
        filename_girls = dirname + str(year) + girls_file
        filename_boys = dirname + str(year) + boys_file
        try:
            myfile = open(filename_girls, 'r')
            with open(filename_girls) as f:
                for line in myfile.readlines():
                    temp = line.split()
                    if temp[0] in temp_dict_girls:
                        temp_dict_girls[temp[0]] += int(temp[1])
                    else:
                        temp_dict_girls[temp[0]] = int(temp[1])
            myfile.close()

            myfile = open(filename_boys, 'r')
            with open(filename_boys) as f:
                for line in myfile.readlines():
                    temp = line.split()
                    if temp[0] in temp_dict_boys:
                        temp_dict_boys[temp[0]] += int(temp[1])
                    else:
                        temp_dict_boys[temp[0]] = int(temp[1])
            myfile.close()
        except:
            print('Error while reading the directory: make sure you wrote a correct year name, try again.')
            quit()

        year += 1

    return max(temp_dict_girls), max(temp_dict_boys)


def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    dirname = dir_path + '/file_utili/BabyNames/'
    first_year = int(input('Insert the first year (4 digits) of the range for which you want to know the most used name: '))
    last_year = int(input('Insert the last year (4 digits) of the range for which you want to know the most used name: '))
    girl, boy = walk(dirname, first_year, last_year)
    print(f'The most used names for girls and boys during the period {first_year}-{last_year} were: {girl} and {boy}')

if __name__ == '__main__':
    main()
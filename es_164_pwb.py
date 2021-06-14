# Gender Neutral Names

import os

def walk(dirname, year):
    neutral_names = []
    temp_list = []
    
    try:
        girls_file = '_GirlsNames.txt'
        boys_file = '_BoysNames.txt'
        filename_girls = dirname + year + girls_file
        filename_boys = dirname + year + boys_file

        # put the girls names in a temporary list
        myfile = open(filename_girls, 'r')
        with open(filename_girls) as f:
            for line in myfile.readlines():
                temp = line.split()
                temp_list.append(temp[0])
        myfile.close()

        #check if the boys names are in the temporary list and add them in the neutral names list
        myfile = open(filename_boys, 'r')
        with open(filename_boys) as f:
            for line in myfile.readlines():
                temp = line.split()
                if temp[0] in temp_list:
                    neutral_names.append(temp[0])
        myfile.close()

        return neutral_names
    except:
        print('Error while reading the directory: make sure you wrote a correct year name, try again.')
        quit()



def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    dirname = dir_path + '/file_utili/BabyNames/'
    year = input('Insert a year (4 digits) for which you want to know the most popular neutral names: ')
    neutral_names = walk(dirname, year)

    if len(neutral_names) == 1:
        print(f'There was a popular neutral name in {year}:', end=' ')
        for name in neutral_names:
            print(name)
    elif len(neutral_names) > 1:
        print(f'There were {len(neutral_names)} popular neutral names in {year}:')
        for name in neutral_names:
            print('•', name)
    else:
        print(f"There wasn't any popular neutral name in {year}.\n")


if __name__ == '__main__':
    main()
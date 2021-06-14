# Names that Reached Number One

import os
# from zipfile import ZipFile

def walk(dirname):
    girls = []
    boys = []
    temp_girls = dict()
    temp_boys = dict()

    try:
        for name in os.listdir(dirname):
            path = os.path.join(dirname, name)
            if os.path.isfile(path):
                if 'Girls' in path:
                    myfile = open(path, 'r')
                    # read the file and insert the names in a temporary list
                    for line in myfile.readlines():
                        temp = line.split()
                        temp_girls[temp[0]] = temp[1]

                    #take the higher values of each year and insert in the right list
                    i = True
                    while i == True :
                        if max(temp_girls) not in girls:
                            girls.append(max(temp_girls))
                            i = False
                        else:
                            temp_girls.pop(max(temp_girls))
                    myfile.close()
                else:
                    myfile = open(path, 'r')
                    # the same for boys
                    for line in myfile.readlines():
                        temp = line.split()
                        temp_boys[temp[0]] = temp[1]

                    #take the higher values of each year and insert in the right list
                    i = True
                    while i == True :
                        if max(temp_boys) not in boys:
                            boys.append(max(temp_boys))
                            i = False
                        else:
                            temp_boys.pop(max(temp_boys))
                    myfile.close()
            else:
                walk(path)

        return girls, boys
    except:
        print('Error while reading the directory: make sure you wrote the right path and folder name.')


def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))

    """    
    * UNZIP THE FILE * 
    filename = dir_path + '/file_utili/baby_names.zip'
    with ZipFile(filename, 'r') as zipObj:
        # Extract all the contents of zip file in current directory
        zipObj.extractall(dir_path + '/file_utili/')
    """
    dirname = dir_path + '/file_utili/BabyNames/'
    girls, boys = walk(dirname)

    print('The most popular names for Girls in the years were:')
    for girl_name in sorted(girls) :
        print('•', girl_name)

    print('\nThe most popular names for Boys in the years were:')
    for boy_name in sorted(boys):
        print('•', boy_name)


if __name__ == '__main__':
    main()
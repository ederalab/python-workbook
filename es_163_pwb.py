# Names that Reached Number One

import os
# from zipfile import ZipFile


def walk(dirname):
    girls = []
    boys = []

    try:
        for name in os.listdir(dirname):
            path = os.path.join(dirname, name)
            if os.path.isfile(path):
                if 'Girls' in path:
                    myfile = open(path, 'r')

                    firstline = myfile.readline()
                    temp = firstline.split()
                    if temp[0] not in girls:
                        girls.append(temp[0])

                    myfile.close()
                else:
                    myfile = open(path, 'r')

                    firstline = myfile.readline()
                    temp = firstline.split()
                    if temp[0] not in boys:
                        boys.append(temp[0])

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
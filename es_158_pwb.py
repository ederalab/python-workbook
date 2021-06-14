# Remove comments

import os

def remove_comments(filename):
    file_to_read = filename.readlines()
    file_to_write = []
    for line in file_to_read:
        if '#' in line:
            remove = line.split('#')
            #print (remove[1])
            new_line = line.replace(remove[1], '')
            line = new_line.replace('#', '\n')
        if line != '' :
            file_to_write.append(line)

    return file_to_write


def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    input_filename = input('Enter the name of the input file: ')
    output_filename = input('Enter the name of the output file: ')
    # input_filename = 'es_14_pwb.py'
    # output_filename = 'es_158_pwb_output.py'
    input_file = dir_path + '/' + input_filename
    ext = output_filename[-3 : ]
    if  ext != '.py':
        ext = '.py'
    output_file = dir_path + '/' + output_filename + ext

    try:
        file_to_read = open(input_file, 'r')
        new_file = remove_comments(file_to_read)
        file_to_read.close()

        file_to_write = open(output_file, 'w')
        for line in new_file:
            file_to_write.write(line)

        file_to_write.close()
        print('Done!')

    except:
        print('File error!')


if __name__ == '__main__':
    main()
    
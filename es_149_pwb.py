# display the head of a file

import sys, os


lines = 10

dir_path = os.path.dirname(os.path.realpath(__file__))

if len(sys.argv) < 2:
    print('Provide the file name as a command line argument')
    quit()

try:
    myfile = open(sys.argv[0], 'r')
    line = myfile.readline()

    count = 0
    while count < lines and line != '':
        line = line.rstrip()
        count += 1

        print(line)
        line = myfile.readline()
    myfile.close()
except IOError:
    print("An error occurred while accessing the file")
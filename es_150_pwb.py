# Display the tail of a File
import sys, os

n_lines = 10

dir_path = os.path.dirname(os.path.realpath(__file__))
#filename = dir_path + '/file_utili/emma.txt'

if len(sys.argv) < 2:
    print('Provide the file name as a command line argument')
    quit()

filename = sys.argv[0]


#SOLUTION 01
def solution01(filename):
    try:
        myfile = open(filename, 'r')
        mylist = []

        count = 0
        for l in myfile:
            line = myfile.readline()
            line = line.rstrip()
            if line != "":
                mylist.append(line)
                count += 1

        myfile.close()

        for i in range(len(mylist) - n_lines, len(mylist)):
            print(mylist[i])

    except IOError:
        print("An error occurred while accessing the file")


#SOLUTION 02

def solution02(filename):
    try:
        myfile = open(filename, 'r')
        file_lines = len(myfile.readlines())
        myfile.close()


        myfile = open(filename, 'r')
        mylines = myfile.readlines()

        for i in range(n_lines + 1, 0, -1):
            print(mylines[file_lines - i])

        myfile.close()

    except IOError:
        print("An error occurred while accessing the file")


#SOLUTION 03

def solution03(filename):
    try:
        myfile = open(filename, 'r')
        mylines = myfile.readlines()
        for i in range(n_lines + 1, 0, -1):
            print(mylines[len(mylines) - i])
        myfile.close()

    except IOError:
        print("An error occurred while accessing the file")


# solution01(filename)
# solution02(filename)
solution03(filename)
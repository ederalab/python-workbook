# Concatenate Multiple Files
import sys, os

dir_path = os.path.dirname(os.path.realpath(__file__))
if len(sys.argv) < 2:
    print('Provide minimum 2 file names as command line arguments')
    quit()

newfile = []

for i in range(len(sys.argv)):
    filename = sys.argv[i]
    myfile = open(filename, 'r')

    line = myfile.readlines()
    newfile.append(line)

    myfile.close()

print(newfile)

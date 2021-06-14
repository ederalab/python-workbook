# Missing comments

import os

def missing_comments():
    dir_path = os.path.dirname(os.path.realpath(__file__))

    for f in os.listdir(dir_path):
        if f[-3:] == '.py':
            try:
                myfile = open(f, 'r')
                prev = " "
                count = 1
                for line in myfile:
                    if line.startswith('def ') and prev[0] != '#':
                        bracket = line.index('(')
                        fname = line[4 : bracket]
                        print(f'file {f}: function {fname} on line {count}')

                    prev = line
                    count += 1
                myfile.close()
            except:
                print(f'Error while opening the file {f}!')



missing_comments()
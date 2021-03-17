#center a string in the terminal window

def centerString(s,w):
    if len(s) >= w:
        return s
    else:
        spaces = (w - len(s) // 2)
        return_string = " " * spaces
        return_string = return_string + s
        return return_string

def main():
    w = 60
    print(centerString("This is my first string.",w))
    print(centerString("Is it centered?",w))
    print(centerString("great!",w))

main()
#the twelve days of christmas

from es_89_pwb import ordinal

def song():
    n = 1
    while n <= 12:
        num = ordinal(n)
        print ("On the",num,"day of Christmas")
        print ("my true love sent to me:")
        
        if n >= 12:
            print("Twelve drummers drumming")
        if n >= 11:
            print("Eleven pipers piping")
        if n >= 10:
            print("Ten lords a-leaping")
        if n >= 9:
            print("Nine ladies dancing")
        if n >= 8:
            print("Eight maids a-milking")
        if n >= 7:
            print("Seven swans a-swimming")
        if n >= 6:
            print("Six geese a-laying")
        if n >= 5:
            print("Five golden rings")
        if n >= 4:
            print("Four calling birds")
        if n >= 3:
            print("Three french hens")
        if n >= 2:
            print("Two turtle doves")
        if n > 1:
            print("And partridge in a pear tree \n")
        if n == 1:
            print("A partridge in a pear tree \n")
        n +=1

song()


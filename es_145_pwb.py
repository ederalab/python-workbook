# scrabble score

def scrabble(s):
    score={'A':1,'E':1,'I':1,'L':1,'N':1,'O':1,'R':1,'S':1,'T':1,'U':1,'D':2,'G':2,'B':3,'C':3,'M':3,'P':3,'F':4,'H':4,'V':4,'W':4,'Y':4,'K':5,'J':8,'X':8,'Q':10,'Z':10}
    count = 0
    s = s.upper()
    for c in s:
        count = count + score[c]

    return count

def main():
    s = input("Insert a word in SCRABBLE game: ")
    score = scrabble(s)
    print("The score of the word",s,"is",score)

if __name__ == '__main__':
    main()

#note to frequency
note = input("enter the note: ")
note = str.upper(note)

if note[0] == "C":
    octave = int(note[1])
    frequency = 261.63
elif note[0] == "D":
    octave = int(note[1])
    frequency = 293.66
elif note[0] == "E":
    octave = int(note[1])
    frequency = 329.63
elif note[0] == "F":
    octave = int(note[1])
    frequency = 349.23
elif note[0] == "G":
    octave = int(note[1])
    frequency = 392.00
elif note[0] == "A":
    octave = int(note[1])
    frequency = 440.00
elif note[0] == "B":
    octave = int(note[1])
    frequency = 493.88

frequency = frequency/2**(4-octave)
print(frequency)

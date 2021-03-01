#frequency to note
frequency = float(input("enter the frequency: "))
c_frequency = 261.63
d_frequency = 293.66
e_frequency = 329.63
f_frequency = 349.23
g_frequency = 392.00
a_frequency = 440.00
b_frequency = 493.88

if frequency >= (c_frequency - 1) and frequency <= (c_frequency + 1):
    print ("This frequency correspond to the note: C")
elif frequency >= (d_frequency - 1) and frequency <= (d_frequency + 1):
    print ("This frequency correspond to the note: D")
elif frequency >= (e_frequency - 1) and frequency <= (e_frequency + 1):
    print ("This frequency correspond to the note: E")
elif frequency >= (f_frequency - 1) and frequency <= (f_frequency + 1):
    print ("This frequency correspond to the note: F")
elif frequency >= (g_frequency - 1) and frequency <= (g_frequency + 1):
    print ("This frequency correspond to the note: G")
elif frequency >= (a_frequency - 1) and frequency <= (a_frequency + 1):
    print ("This frequency correspond to the note: A")
elif frequency >= (b_frequency - 1) and frequency <= (b_frequency + 1):
    print ("This frequency correspond to the note: B")
else:
    print("This frequency doesn't correspond to a known note")


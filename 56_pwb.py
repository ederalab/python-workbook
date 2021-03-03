#frequency to name
fr = float(input("Insert the frequency range: "))

if fr < (3 * 10**9):
    name = "radio waves"
elif fr >= (3 * 10**9) and fr < (3 * 10**12):
    name = "microwaves"
elif fr >= (3 * 10**12) and fr < (4.3 * 10**14):
    name = "infrared light"
elif fr >= (4.3 * 10**14) and fr < (7.5 * 10**14):
    name = "visible light"
elif fr >= (7.5 * 10**14) and fr < (3 * 10**17):
    name = "ultraviolet light"
elif fr >= (3 * 10**17) and fr < (3 * 10**19):
    name = "x-rays"
elif fr >= (3 * 10**19):
    name = "gamma rays"

print(fr,"Hz is the frequency of",name)
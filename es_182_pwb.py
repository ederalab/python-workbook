# spelling with element symbols

def chemical_elements():
    elements_table = {
    'H' : 'Hydrogen', 'He' : 'Helium', 'Li' : 'Lithium', 'Be' : 'Beryllium', 'B' : 'Boron',
    'C' : 'Carbon', 'N' : 'Nitrogen', 'O' : 'Oxygen', 'F' : 'Fluorine', 'Ne' : 'Neon',
    'Na' : 'Sodium', 'Mg' : 'Magnesium', 'Al' : 'Aluminum', 'Si' : 'Silicon', 'P' : 'Phosphorus',
    'S' : 'Sulfur', 'Cl' : 'Chlorine', 'Ar' : 'Argon', 'K' : 'Potassium', 'Ca' : 'Calcium',
    'Sc' : 'Scandium', 'Ti' : 'Titanium', 'V' : 'Vanadium', 'Cr' : 'Chromium', 'Mn' : 'Manganese',
    'Fe' : 'Iron', 'Co' : 'Cobalt', 'Ni' : 'Nickel', 'Cu' : 'Copper', 'Zn' : 'Zinc',
    'Ga' : 'Gallium', 'Ge' : 'Germanium', 'As' : 'Arsenic', 'Se' : 'Selenium', 'Br' : 'Bromine',
    'Kr' : 'Krypton', 'Rb' : 'Rubidium', 'Sr' : 'Strontium', 'Y' : 'Yttrium', 'Zr' : 'Zirconium',
    'Nb' : 'Niobium', 'Mo' : 'Molybdenum', 'Tc' : 'Technetium', 'Ru' : 'Ruthenium', 'Rh' : 'Rhodium',
    'Pd' : 'Palladium', 'Ag' : 'Silver', 'Cd' : 'Cadmium', 'In' : 'Indium', 'Sn' : 'Tin', 'Sb' : 'Antimony',
    'Te' : 'Tellurium', 'I' : 'Iodine', 'Xe' : 'Xenon', 'Cs' : 'Caesium', 'Ba' : 'Barium', 'La' : 'Lanthanum',
    'Ce' : 'Cerium', 'Pr' : 'Praseodymium', 'Nd' : 'Neodymium', 'Pm' : 'Promethium', 'Sm' : 'Samarium', 'Eu' : 'Europium',
    'Gd' : 'Gadolinium', 'Tb' : 'Terbium', 'Dy' : 'Dysprosium', 'Ho' : 'Holmium', 'Er' : 'Erbium', 'Tm' : 'Thulium',
    'Yb' : 'Ytterbium', 'Lu' : 'Lutetium', 'Hf' : 'Hafnium', 'Ta' : 'Tantalum', 'W' : 'Tungsten', 'Re' : 'Rhenium',
    'Os' : 'Osmium', 'Ir' : 'Iridium', 'Pt' : 'Platinum', 'Au' : 'Gold', 'Hg' : 'Mercury', 'Tl' : 'Thallium', 'Pb' : 'Lead',
    'Bi' : 'Bismuth', 'Po' : 'Polonium', 'At' : 'Astatine', 'Rn' : 'Radon', 'Fr' : 'Francium', 'Ra' : 'Radium', 'Ac' : 'Actinium',
    'Th' : 'Thorium', 'Pa' : 'Protactinium', 'U' : 'Uranium', 'Np' : 'Neptunium', 'Pu' : 'Plutonium', 'Am' : 'Americium',
    'Cm' : 'Curium', 'Bk' : 'Berkelium', 'Cf' : 'Californium', 'Es' : 'Einsteinium', 'Fm' : 'Fermium', 'Md' : 'Mendelevium',
    'No' : 'Nobelium', 'Lr' : 'Lawrencium', 'Rf' : 'Rutherfordium', 'Db' : 'Dubnium', 'Sg' : 'Seaborgium', 'Bh' : 'Bohrium',
    'Hs' : 'Hassium', 'Mt' : 'Meitnerium', 'Ds' : 'Darmstadtium', 'Rg' : 'Roentgenium', 'Cn' : 'Copernicium', 'Nh' : 'Nihonium',
    'Fl' : 'Flerovium', 'Mc' : 'Moscovium', 'Lv' : 'Livermorium', 'Ts' : 'Tennessine', 'Og' : 'Oganesson'
}
    symbols = []

    for s in elements_table:
        symbols.append(s.lower())

    return symbols


def chemical_spelling (word, symbols):
    check = []
    for i in range(len(word)):
        if word[i] in symbols and word[i-1] + word[i] not in check:
            check.append(word[i])
        elif i < (len(word)-1) and word[i] + word[i+1] in symbols:
            word.replace(word[i+1],'')
            check.append(word[i] + word[i+1])

    spelling = '.'.join(check)

    if (''.join(check) == word):
        return True, spelling
    else:
        return False, ''


def main():
    symbols = chemical_elements()
    word = input("Insert a word and I'll spell it with chemical symbols: ")
    result, spelling = chemical_spelling(word, symbols)
    if result:
        print(f"The word {word} can be spelled {spelling}")
    else:
        print(f"The word {word} can't be spelled with chemical elements")


if __name__ == '__main__':
    main()

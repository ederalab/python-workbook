# element sequences
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
    elements = []

    for k in elements_table:
        v = elements_table[k]
        elements.append(v.lower())
    return elements

#elementi
def element_sequence(start, elements):
    if start == "" :
        return []

    best = []
    last = start[len(start) - 1].lower()

    for i in range(0, len(elements)):
        first = elements[i][0].lower()

        if first == last :
            seq = element_sequence(elements[i], elements[0 : i] + elements[i + 1 : len(elements)])

            if len(seq) > len(best):
                best = seq

    return [start] + best

# main
def main():
    elements = chemical_elements()
    element = input("Enter the name of an element: ")
    element.lower()

    if element in elements :
        elements.remove(element)
        sequence = element_sequence(element, elements)
        print(f"The longest sequence starting with {element} is: ")

        for el in sequence :
            print(" ", el)
    else:
        print(f"Sorry, but {element} is not a valid element name.")


if __name__ == '__main__':
    main()
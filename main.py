from pyscript import document

# symbol: (name, atomic number, atomic mass)
ELEMENTS = {
    "H":  ("Hydrogen", 1, 1.008),
    "He": ("Helium", 2, 4.0026),
    "C":  ("Carbon", 6, 12.011),
    "N":  ("Nitrogen", 7, 14.007),
    "O":  ("Oxygen", 8, 15.999),
    "F":  ("Fluorine", 9, 18.998),
    "Ne": ("Neon", 10, 20.180),
    "P":  ("Phosphorus", 15, 30.974),
    "S":  ("Sulfur", 16, 32.06),
    "Cl": ("Chlorine", 17, 35.45),
    "Ar": ("Argon", 18, 39.948),
    "Se": ("Selenium", 34, 78.971),
    "Br": ("Bromine", 35, 79.904),
    "Kr": ("Krypton", 36, 83.798),
    "I":  ("Iodine", 53, 126.904),
    "Xe": ("Xenon", 54, 131.293),
    "Rn": ("Radon", 86, 222),
}


def element_checker(event):
    input_box = document.querySelector("#element_name")
    result = document.querySelector("#result")

    raw = input_box.value.strip()

    if raw == "":
        result.innerHTML = "<span class='text-danger'>Please enter an element symbol.</span>"
        return

    # Normalize: first letter uppercase, second lowercase (e.g. "cl" -> "Cl")
    symbol = raw[0].upper() + raw[1:].lower()

    if symbol in ELEMENTS:
        name, number, mass = ELEMENTS[symbol]
        result.innerHTML = (
            f"<b>Symbol:</b> {symbol}<br>"
            f"<b>Element:</b> {name}<br>"
            f"<b>Atomic Number:</b> {number}<br>"
            f"<b>Atomic Mass:</b> {mass}"
        )
    else:
        result.innerHTML = (
            f"<span class='text-danger'>'{raw}' is not a recognized non-metal "
            f"element symbol.</span>"
        )


# stores data for a measurement unit
class Unit:

    def __init__(self: object, name: str, symbol: str, top: float, bottom: float = 0, plural: str = ""):
        # markers so we know which unit is which
        self.name   = name
        self.symbol = symbol
        # top and bottom of the scales (celsius 0-100, fahrenheit 32-212, etc...)
        # top goes first so we dont have to specify bottom scale being 0 every time
        self.top    = top
        self.bottom = bottom
        # special handling for plural form
        if len(plural) > 0 and not(plural.isalpha()): self.plural = name
        else: self.plural = name + "s" if plural == "" else plural
    
    # for sorting
    @staticmethod
    def key(unit: object) -> int: return unit.top + unit.bottom
    
    # converts a value from one unit to another
    @staticmethod
    def convert(value: float, origin: object, output: object) -> float:
        A: float = origin.top - value
        B: float = origin.top - origin.bottom
        D: float = output.top - output.bottom
        return output.top - (A * D / B)

# build display of units (assuming they are sorted)
def build_display(units: list[Unit]) -> str:
    # this will be used for formatting
    longest_name: int = -1
    counter: int = 0
    for unit in units:
        longest_name = max(longest_name, len(unit.plural))
        counter += 1

    output: str = ""
    counter = 0
    # compensate for the actual index printing
    compensate_index: int = len(str(len(units) - 1))
    for unit in units:
        output += f"{str(counter).rjust(compensate_index)} - {unit.plural.ljust(longest_name + 1)} ({unit.symbol})\n"
        counter += 1
    return output

# convert integer to corresponding key in dictionary
def int2key(index: int, dictionary: dict) -> any:
    if index < 0 or index > len(dictionary): raise ValueError()
    counter: int = 0
    for key in dictionary:
        if type(key) == int: return index
        if counter == index: return key
        counter += 1
    raise IndexError(f"Index out of bounds ({len(dictionary)}): {index}")

def get_int(ask: str, valid_range: range = None) -> int:
    while True:
        text: str = input(f"{ask}\n>>> ")
        if text.isdigit():
            result = int(text)
            if valid_range == None or result in valid_range: return result
        print("\nInvalid input")

def convert() -> bool:
    # DO NOT CHANGE!!!
    THOUSAND: int   = 1000
    MILE2MM:  int   = 1609344
    KG2LB:    float = 2.2046226218
    SQUARE60: int   = 60 ** 2

    # massive table of units
    units: dict[str, list[Unit]] = {
        "distance": [
            Unit("mile",                  "mi",   1),
            Unit("kilometer",             "km",   MILE2MM / THOUSAND ** 2),
            Unit("meter",                 "m",    MILE2MM / 1000),
            Unit("yard",                  "yd",   1760),
            Unit("foot",                  "ft",   5280,             plural = "feet"),
            Unit("inch",                  "in",   63360,            plural = "inches"),
            Unit("centimeter",            "cm",   MILE2MM / 10),
            Unit("millimeter",            "mm",   MILE2MM),
            Unit("thousandth of an inch", "thou", 63360 * THOUSAND, plural = "thousandths of an inch"),
            Unit("micrometer",            "um",   MILE2MM * THOUSAND),
            Unit("nanometer",             "nm",   MILE2MM * THOUSAND ** 2),
            Unit("angstrom",              "a",    MILE2MM * THOUSAND ** 2 * 10)
        ],
        "mass": [
            Unit("long ton",         "lt", KG2LB / 2240),
            Unit("metric ton",       "t",  1 / THOUSAND),
            Unit("short ton",        "tn", KG2LB / THOUSAND / 2),
            Unit("UK hundredweight", "UK cwt", KG2LB * 112, plural = "."),
            Unit("US hundredweight", "US cwt", KG2LB * 100, plural = "."),
            Unit("stone",            "st", KG2LB * 14),
            Unit("kilogram",         "kg", 1),
            Unit("pound",            "lb", KG2LB),
            Unit("ounce",            "oz", 35.2739619496),
            Unit("gram",             "g",  THOUSAND),
            Unit("grain",            "gr", KG2LB * THOUSAND * 7),
            Unit("milligram",        "mg", THOUSAND ** 2),
            Unit("microgram",        "ug", THOUSAND ** 3),
            Unit("nanogram",         "ng", THOUSAND ** 4)
        ],
        "temperature": [
            Unit("newton",     "*N",  33,       plural = "."),
            Unit("romer",      "*Ro", 60,       7.5,     "."),
            Unit("reaumur",    "*Re", 80,       plural = "."),
            Unit("celsius",    "*C",  100,      plural = "."),
            Unit("delisle",    "*De", 0,        150,     "."),
            Unit("fahrenheit", "*F",  212,      32,      "."),
            Unit("kelvin",     "K",   373.1339, 273.15,  "."),
            Unit("rankine",    "*Ra", 671.641,  491.67,  ".")
        ],
        "time": [
            Unit("week",        "N/A", 1 / 24 / 7),
            Unit("day",         "d",   1 / 24),
            Unit("hour",        "h",   1),
            Unit("minute",      "m",   60),
            Unit("second",      "s",   SQUARE60),
            Unit("milisecond",  "ms",  SQUARE60 * THOUSAND),
            Unit("microsecond", "us",  SQUARE60 * THOUSAND ** 2),
            Unit("nanosecond",  "ns",  SQUARE60 * THOUSAND ** 3)
        ]
    }
    # sort them in ascending order
    for unit_list in units.values(): unit_list.sort(key = lambda unit: unit.top + unit.bottom)

    # formatting
    print()

    # print available types of units
    index: int = 0
    for unit_type in units:
        print(f"{index} - {unit_type}")
        index += 1
    
    selected_type: list[Unit] = units[int2key(get_int("Select a unit type", range(len(units))), units)]

    # ask for origin unit
    print()
    selected_origin_int: int = get_int(f"Select the value origin\n{build_display(selected_type)}", range(len(selected_type)))
    selected_origin: Unit = selected_type[selected_origin_int]
    
    # ask for value
    print()
    value: float = 0
    ALLOWED: str = ".0123456789"
    while True:
        text: str = input(f"Enter value in {selected_origin.plural}\n>>> ")
        valid: bool = True

        if len(text) == 0: valid = False
        for char in text:
            if ALLOWED.find(char) == -1:
                valid = False
                break
        
        if not(valid):
            print("\nInvalid input")
            continue

        value = float(text)
        break

    # ask for output unit
    print()
    selected_type.remove(selected_origin)
    selected_output_int: int = get_int(f"Select the output unit\n{build_display(selected_type)}", range(len(selected_type)))
    selected_output: Unit = selected_type[selected_output_int]

    # display result with specified accuracy
    print()
    accuracy: int = get_int("How much accuracy? (in digits after the decimal)")

    conversion_result: float = round(Unit.convert(value, selected_origin, selected_output), accuracy)
    print(f"{value} {selected_origin.name if value == 1 else selected_origin.plural} is (approx.) {conversion_result} {selected_output.name if conversion_result == 1 else selected_output.plural}")

    # ask to convert again
    print()
    while True:
        text: str = input("Do you want to convert again? (y/n)\n>>> ").strip().lower()
        valid: bool = text == "y" or text == "n"
        if not(valid):
            print("\nInvalid input")
            continue
        return text == "y"

def main() -> None:
    restart: bool = True
    while restart: restart = convert()

if __name__ == "__main__": main()

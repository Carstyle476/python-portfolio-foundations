
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

        # special handling for plural form (to be grammatically correct)
        if len(plural) > 0 and not(check_allowed(plural.lower(), " abcdefghijklmnopqrstuvwxyz")): self.plural = name
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


# check if every character in "string" exists in "allowed"
def check_allowed(string: str, allowed: str) -> bool:
    for char in string:
        if allowed.find(char) == -1: return False
    return True


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


# get an integer input from user
def get_int(ask: str, valid_range: range = None) -> int:
    while True:
        text: str = input(f"{ask}\n>>> ")
        if text.isdigit():
            result = int(text)
            if valid_range == None or result in valid_range: return result
        print("\nInvalid input")


def convert() -> bool:
    # DO NOT CHANGE!!!
    TWELVE:    int   = 12
    THOUSAND:  int   = 1000
    MILLION:   int   = THOUSAND ** 2
    BILLION:   int   = MILLION * THOUSAND
    SQUARE60:  int   = 3600
    WEEK2HOUR: float = 24 * 7

    MILE2MM:   int   = 1609344
    MILE2KM:   int   = MILE2MM / MILLION
    MILE2YARD: int   = 1760
    MILE2INCH: int   = 63360

    KG2LB:     float = 2.2046226218
    LB2GRAIN:  float = KG2LB * THOUSAND * 7


    # massive table of units
    units: dict[str, list[Unit]] = {
        "distance": [
            # not exactly metric
            Unit("league",                "le",   1 / 3),
            Unit("nautical mile",         "nmi",  MILE2KM / 1.852),
            Unit("mile",                  "mi",   1),
            Unit("cable",                 "cb",   MILE2YARD / TWELVE / 20),
            Unit("fathom",                "ftm",  MILE2YARD / 2),
            Unit("yard",                  "yd",   MILE2YARD),
            Unit("foot",                  "ft",   MILE2YARD * 3,        plural = "feet"),
            Unit("hand",                  "h",  MILE2INCH / 4),
            Unit("inch",                  "in",   MILE2INCH,            plural = "inches"),
            Unit("pica",                  "P",    MILE2INCH * 6),
            Unit("point",                 "p",    MILE2INCH * TWELVE * 6),
            Unit("thousandth of an inch", "thou", MILE2INCH * THOUSAND, plural = "thousandths of an inch"),
            Unit("twip",                  "twip", MILE2INCH * TWELVE ** 2 * 10),
            # metric
            Unit("kilometer",             "km",   MILE2KM),
            Unit("meter",                 "m",    MILE2MM / THOUSAND),
            Unit("centimeter",            "cm",   MILE2MM / 10),
            Unit("millimeter",            "mm",   MILE2MM),
            Unit("micrometer",            "um",   MILE2MM * THOUSAND),
            Unit("nanometer",             "nm",   MILE2MM * MILLION),
            Unit("angstrom",              "A",    MILE2MM * MILLION * 10)
        ],
        "mass": [
            # not exactly metric
            Unit("long ton",            "lt",     KG2LB / 2240),
            Unit("short ton",           "tn",     KG2LB / THOUSAND / 2),
            Unit("long hundredweight",  "UK cwt", KG2LB / 112, plural = "."),
            Unit("short hundredweight", "US cwt", KG2LB / 100, plural = "."),
            Unit("stone",               "st",     KG2LB / 14,  plural = "."),
            Unit("pound",               "lb",     KG2LB),
            Unit("troy pound",          "lb t",   LB2GRAIN / TWELVE ** 2 / 40),
            Unit("troy ounce",          "oz t",   LB2GRAIN / TWELVE / 40),
            Unit("ounce",               "oz",     KG2LB * 16),
            Unit("dram",                "dr",     KG2LB * 256),
            Unit("carat",               "ct",     MILLION / 200),
            Unit("pennyweight",         "dwt",    LB2GRAIN / TWELVE / 2),
            Unit("grain",               "gr",     LB2GRAIN),
            # metric
            Unit("metric ton",          "t",      1 / THOUSAND),
            Unit("kilogram",            "kg",     1),
            Unit("gram",                "g",      THOUSAND),
            Unit("milligram",           "mg",     MILLION),
            Unit("microgram",           "ug",     BILLION),
            Unit("nanogram",            "ng",     MILLION ** 2)
        ],
        "temperature": [
            Unit("newton",     "*N",  33,     plural = "."),
            Unit("romer",      "*Ro", 60,     7.5,     "."),
            Unit("reaumur",    "*Re", 80,     plural = "."),
            Unit("celsius",    "*C",  100,    plural = "."),
            Unit("delisle",    "*De", 0,      150,     "."),
            Unit("fahrenheit", "*F",  212,    32,      "."),
            Unit("kelvin",     "K",   373.15, 273.15,  "."),
            Unit("rankine",    "*Ra", 671.67, 491.67,  ".")
        ],
        "time": [
            Unit("week",        "N/A", 1),
            Unit("day",         "d",   7),
            Unit("hour",        "h",   WEEK2HOUR),
            Unit("minute",      "m",   WEEK2HOUR * 60),
            Unit("second",      "s",   WEEK2HOUR * SQUARE60),
            Unit("milisecond",  "ms",  WEEK2HOUR * SQUARE60 * THOUSAND),
            Unit("microsecond", "us",  WEEK2HOUR * SQUARE60 * MILLION),
            Unit("nanosecond",  "ns",  WEEK2HOUR * SQUARE60 * BILLION)
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
    while True:
        text: str = input(f"Enter value in {selected_origin.plural}\n>>> ")
        if len(text) > 0 and check_allowed(text, ".0123456789"):
            value = float(text)
            break
        print("\nInvalid input")

    # ask for output unit
    print()
    selected_type.remove(selected_origin)
    selected_output_int: int = get_int(f"Select the output unit\n{build_display(selected_type)}", range(len(selected_type)))
    selected_output: Unit = selected_type[selected_output_int]

    # display result with specified accuracy (if needed)
    print()
    conversion_result:  float = Unit.convert(value, selected_origin, selected_output)
    rounded_conversion: int   = round(conversion_result)
    accuracy: int = 0 if rounded_conversion == conversion_result else get_int("How much accuracy? (in digits after the decimal)")

    rounded_value: int = round(value)
    print(f"{rounded_value if rounded_value == value else value} {selected_origin.name if value == 1 else selected_origin.plural} is {rounded_conversion if accuracy == 0 else f'approximately {round(conversion_result, accuracy)}'} {selected_output.name if conversion_result == 1 else selected_output.plural}")

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
    while restart:
        # wrap the entire program in a try/except block just for ctrl+c exit (yikes)
        try: restart = convert()
        except KeyboardInterrupt: break
    print("\nExiting...")

if __name__ == "__main__": main()

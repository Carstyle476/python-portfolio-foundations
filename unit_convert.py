
# stores data for a measurement unit
class Unit:

    def __init__(self: object, bottom: float, top: float):
        # bottom and top of the scales (celsius 0-100, fahrenheit 32-212, etc...)
        self.bottom = bottom
        self.top    = top
    
    # converts a value from one unit to another
    @staticmethod
    def convert(value: float, unit_from: object, unit_to: object) -> float:
        return value * (unit_from.top - unit_from.bottom) / (unit_to.top - unit_to.bottom) + (unit_to.bottom - unit_from.bottom)

def main() -> None:
    pass

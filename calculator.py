
from math import *
import sys

# interpret an input string (with the help of eval())
def calculate(current: float, string: str) -> float:
    ALLOWED: str = ".0123456789+-*/()"

    # check whether to modify current number or overwrite it with result of input expression
    modify_current: bool = False
    for char in string:
        if char == " ": continue
        if ALLOWED.find(char) == -1: raise SyntaxError(f"Unsupported character found: {char}")
        if ALLOWED[11:].find(char) != -1:
            modify_current = True
            break
        if ALLOWED[:11].find(char) != -1: break
    
    # spit out the result
    return eval(f"{current if modify_current else ''}{string}")

def main() -> None:
    current: float = 0
    text:    str   = ""
    tips:    bool  = True

    # replicate actual calculator behavior
    while True:
        try:
            temp_text = text
            temp_input = input(f"{'\nt to display this\ne to exit\nenter to repeat operation\n' if tips else ''}\n{current}\n>>> ")
            if temp_input == "e": return
            if temp_input == "t":
                tips = True
                continue

            if temp_input != "": temp_text = temp_input
            current = calculate(current, temp_text)
            text = temp_text
        except: print(f"An error occured:\n{repr(sys.exception())}")
        tips = False

if __name__ == "__main__": main()

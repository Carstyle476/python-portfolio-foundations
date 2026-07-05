
from math import *

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
        exit: bool = False

        try:
            temp_text = text
            temp_input = input(f"{'\nt to display these tips\ne to exit\nenter to repeat operation\n' if tips else ''}\n{current}\n>>> ")
            # "regular" exit
            if temp_input == "e": exit = True
            if temp_input == "t":
                tips = True
                continue

            if temp_input != "": temp_text = temp_input
            current = calculate(current, temp_text)
            text = temp_text
        # ctrl+c exit
        except KeyboardInterrupt: exit = True
        # eval() threw an error
        except Exception as e: print(f"An error occured:\n{repr(e)}")

        # exit mechanism
        if exit:
            print("\nExiting...")
            return
        
        # disable tips
        tips = False

if __name__ == "__main__": main()

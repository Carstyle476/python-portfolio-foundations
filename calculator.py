
from math import factorial
import sys

def calculate(current: float, string: str) -> float:
    ALLOWED:        str   = ".0123456789+-*/^!"
    operation_char: str   = ""
    num_build_temp: str   = ""
    prev_char:      str   = ""
    operation_num1: float = current
    operation_num2: float = current
    num1_built:     bool  = False
    num2_built:     bool  = False
    # 0 - operation
    # 1 - number
    prev_type:      int   = -1

    # go through every character
    for char in string:
        # ignore spaces
        if char == " ":
            continue

        # complain if there's something it doesn't know
        if ALLOWED.find(char) == -1: raise SyntaxError(f"Unsupported character found: {char}")

        # operation
        if char in ALLOWED[11:]:
            if operation_char != "": raise SyntaxError("More than one operation found")
            operation_char += char

            if num_build_temp != "":
                if not(num1_built):
                    operation_num1 = float(num_build_temp)
                    num1_built = True
                elif not(num2_built):
                    operation_num2 = float(num_build_temp)
                    num2_built = True
            
            num_build_temp = ""
            prev_type = 0
        # number
        else:
            if prev_type == 1 and prev_char == " ": raise SyntaxError("Gap in number found")
            num_build_temp += char
            prev_type = 1
    
    # TODO: dont repeat this block of code
    if num_build_temp != "":
        if not(num1_built):
            operation_num1 = float(num_build_temp)
            num1_built = True
        elif not(num2_built):
            operation_num2 = float(num_build_temp)
            num2_built = True
    
    # complain again
    if not(num1_built): raise ValueError("No operands found")
    if operation_char == "": return operation_num1
    
    # the actual calculation
    numbers: list[int] = [
        current if not(num2_built) else operation_num1,
        operation_num1 if not(num2_built) else operation_num2
    ]
    if operation_char == "+": numbers[0] += numbers[1]
    if operation_char == "-": numbers[0] -= numbers[1]
    if operation_char == "*": numbers[0] *= numbers[1]
    if operation_char == "/": numbers[0] /= numbers[1]
    if operation_char == "^": numbers[0] **= numbers[1]
    if operation_char == "!":
        if num2_built: raise SyntaxError("More than 1 operand inputted for factorial")
        if round(numbers[0]) != numbers[0]: raise TypeError("Non-integer operand inputted for factorial")
        numbers[0] = factorial(numbers[0])

    return numbers[0]

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

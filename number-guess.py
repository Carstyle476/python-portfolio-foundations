
# import stuff we need
from random import randint
from time import sleep

# main function
def main() -> None:
    # variables
    LOWER: int = 1
    UPPER: int = 100
    attempts: int = 0
    target: int = randint(LOWER, UPPER)
    guess: int = -1

    print("Guess a number between 1 and 100 (inclusive)")

    # guessing loop
    while guess != target:
        # handle non-integer inputs
        try:
            text_input = input(">>> ").strip()
            if not(text_input.isdigit()): raise TypeError()
            guess = int(text_input)
            if guess < LOWER or guess > UPPER: raise ValueError()
        except TypeError:
            print("Not a valid number, try again")
            continue
        except ValueError:
            print(f"Number {f'below {LOWER}' if guess < LOWER else f'above {UPPER}'}, try again")
            continue
        
        attempts += 1
        if guess < target: print("Too low, try again")
        elif guess > target: print("Too high, try again")
        else: print(f"You got it! The number was {target}\nYou took {attempts} attempts")
    sleep(4)

# this file is meant to be executed
if __name__ == "__main__": main()

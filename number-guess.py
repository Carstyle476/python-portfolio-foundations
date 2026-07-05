
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

    print("\nGuess a number between 1 and 100 (inclusive)\n(leave blank to exit)")

    # guessing loop
    while guess != target:
        exit: bool = False

        # handle invalid inputs
        try:
            text_input = input(">>> ").strip()
            if not(text_input.isdigit()):
                if text_input == "": exit = True
                else: raise TypeError()
            else:
                guess = int(text_input)
                if guess < LOWER or guess > UPPER: raise ValueError()
        # ctrl+c exit
        except KeyboardInterrupt: exit = True
        # not a number
        except TypeError:
            print("Not a valid number, try again")
            continue
        except ValueError:
        # number out of range
            print(f"Number {f'below {LOWER}' if guess < LOWER else f'above {UPPER}'}, try again")
            continue

        # actual exit mechanism
        if exit:
            print("\nExiting...")
            return
        
        # print the result
        attempts += 1
        if guess < target: print("Too low, try again")
        elif guess > target: print("Too high, try again")
        else: print(f"You got it! The number was {target}\nYou took {attempts} attempts")
    # (for 4 seconds, so user can actually read it)
    sleep(4)

if __name__ == "__main__": main()

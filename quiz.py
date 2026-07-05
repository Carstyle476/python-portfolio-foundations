
from re import match
from time import time, sleep
from random import shuffle

# regex to match yes answers
YES: str = "y[eahps]*"

# MASSIVE table of questions and their answers
# the answers are stored in either direct or regular expression form
# False = direct
# True = regex
# if True, the 2nd element in the list is for displaying the "correct" answer
def questions_answers() -> dict[str, tuple[bool, list[str]]]:
    return {
        # rotor wash, downwash, rotor downwash, wash (unavoidable)
        "What is the term for the fast-moving air underneath a helicopter?":
        (True, ["((rotor)?[ ]?(down)?){1}[ -]*wash", "rotor wash"]),

        "What integer is the irrational number 'Pi' closest to?":
        (False, ["3", "three"]),

        # 22, twenty two, twenty-two, twenty 2, 20 two
        "How many keywords does Lua 5.5 have?":
        (True, ["(22|((20|twenty){1}[ -]*(2|two){1})){1}", "22"]),

        # 2, 2nd, second, 2 place (unavoidable), 2nd place, second place
        "If you're in a race and you overtake the person in 2nd, what place are you in now?":
        (True, ["(2|2nd|second){1}[ -]?(place)?", "2nd"]),

        "How many .py files are in Carstyle476's 'python-portfolio-foundations' GitHub repository?":
        (False, ["6", "six"]),

        "What is the name of the fictional city in Need for Speed(tm): Most Wanted (the 2005 game)?":
        (False, ["rockport"]),

        # y (for yes)
        "Is SQL mainly used for databases? (yes/no)":
        (True, [YES, "yes"]),

        "Which country's flag looks like a flipped Indonesian flag?":
        (False, ["poland", "polska", "republic of poland", "rzeczpospolita polska"]),

        "Which COUNTRY is the only one with a non-rectangular flag?":
        (False, ["nepal", "republic of nepal", "federal democratic republic of nepal"]),

        "What is 'Germany' in the German language?":
        (False, ["deutschland"])
    }

# main quiz function
def quiz(show: bool) -> None:
    # get question/answer list and shuffle them
    # (these are some pretty long types...)
    questions:  dict[str, tuple[bool, list[str]]]        = questions_answers()
    q_list:     list[tuple[str, tuple[bool, list[str]]]] = list(questions.items())
    shuffle(q_list)
    questions = dict(q_list)

    # keep track of score
    score:     int = 0

    # flags
    exit:    bool = False
    started: bool = False
    # start gets time() now as fallback in case i missed something
    start: float = time()
    # loop over every question
    for i in questions:
        correct: bool = False

        # get answer from user
        # for internal comparison, make it lowercase and remove any spaces at start and end
        try:
            given_answer:   str = input(f"\n{i}\n>>> ").lower().strip()
            correct_answer: tuple[bool, list[str]] = questions[i]

            if given_answer == "":
                exit = True
                break

            # handle direct vs regex questions
            if correct_answer[0]: correct = match(correct_answer[1][0], given_answer) != None
            else:
                for answer in correct_answer[1]:
                    if answer == given_answer:
                        correct = True
                        break

            # display result
            if correct:
                score += 1
                print(f"Correct! Your score: {score}")
            else:
                # this is compressible but it'll become an f-string inside an f-string
                # i have questionable formatting habits but that's too much for me (or anyone for that matter)
                # not good
                correct_display: str = f"\nThe correct answer was: {correct_answer[1][1 if correct_answer[0] else 0]}"
                print(f"Wrong...{correct_display if show else ''}")
        # exit cleanly if ctrl+c exit
        except KeyboardInterrupt:
            exit = True
            break

        # start the timer only when the 1st question is answered
        if not(started):
            started = True
            start = time()
    # record how long it took
    stop: float = time()

    # exit mechanism
    if exit:
        print("\nExiting...")
        return
    
    # display results
    print("\nResults:")
    print(f"You were able to answer {score}/{len(questions)} questions in {round(stop - start, 3)} seconds.")
    sleep(5)

# settings and quiz start is handled here
def main() -> None:
    show_option_input: str = input("\nPop quiz!\nDo you want correct answers to be displayed if answered incorrectly? (yes/no)\n>>> ")
    print("Remember:\n- Leave blank to exit prematurely\n- DO NOT MAKE TYPOS! This program doesn't check for them")
    # handling the "show incorrect answers" option
    quiz(match(YES, show_option_input))

if __name__ == "__main__": main()

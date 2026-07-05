
from random import randint

def templates_list() -> list[str]:
    return [
"""
Every morning, MALE_NAME wakes up at CLOCK_TIME.
He gets out of SINGULAR_NOUN, brushes his SINGULAR_NOUN, and takes a ADJECTIVE SINGULAR_NOUN.
Then he puts on his PLURAL_NOUN and eats FOOD for breakfast.

After breakfast, he SINGULAR_VERB to work.
During his lunch break, he likes to VERB at the ADJECTIVE PLACE.
In the evening, he cooks FOOD for dinner before PASTIME and going to sleep.
""",
"""
One morning, MALE_NAME realized he couldn't VERB his SINGULAR_NOUN.
He looked under the SINGULAR_NOUN, inside his SINGULAR_NOUN, and even in the ROOM where he had PAST_VERB.
Then he remembered PRESENT_VERB it into his SINGULAR_NOUN PAST_TIME_REFERENCE.

He ADVERB PAST_TENSE_VERB upstairs and ADVERB searched every SINGULAR_NOUN.
Finally, he found it hidden beneath a SINGULAR_NOUN.
Feeling EMOTION, he PAST_VERB his SINGULAR_NOUN and left for work just in time.
""",
"""
At the edge of an old PLACE stood an abandoned TYPE_OF_BUILDING that no one had PAST_VERB for TIME_LENGTH.
One ADJECTIVE afternoon, FEMALE_NAME pushed open the SINGULAR_NOUN and PAST_VERB inside.

In the corner, she noticed a dusty ANTIQUE_OBJECT covered by a SINGULAR_NOUN.
She carefully PAST_TENSE_VERB it and discovered beautiful PLURAL_NOUN carved into its OBJECT_ATTRIBUTE.
A small NOUN was attached to it with a rusty NOUN.

The writing said the object had belonged to a famous OCCUPATION over PAST_TIME_REFERENCE.
She PAST_FACIAL_EXPRESSION with EMOTION, knowing she had PAST_VERB a piece of history.
"""
    ]

def mad_libs(template: str) -> None:

    print("\nFill in the blanks, leave blank to quit to options")

    # keep track of stuff
    word: str = ""
    result: str = ""
    completed: bool = False

    # go over every character
    ALPHABET: str = "abcdefghijklmnopqrstuvwxyz_"
    for i in range(len(template)):
        # stop building if the word stops
        if ALPHABET.find(template[i].lower()) == -1:
            if word.isupper():
                word = input(f"\nEnter a{'n' if word[0] != 'A' and 'AEIOU'.find(word[0]) != -1 else ''} {word.lower().replace("_", " ")}\n>>> ").strip()
                # for exiting
                if word == "": return
            result += f"{word}{template[i]}"
            word = ""
        # build up the current word
        else: word += template[i]
        if i == len(template) - 1: completed = True
    
    if completed: print(result)

def main() -> None:
    templates: list[str] = templates_list()
    pick: int = -1

    # keep going until user wants to exit
    while True:
        can_retry: bool = pick >= 0
        text: str = input(f"\np - play new{'\nr - retry same' if can_retry else ''}\ne - exit\nSelect an option\n>>> ")
        # play a new game
        if text == "p":
            if pick == -1: pick = randint(0, len(templates) - 1)
            pick += 1
            pick %= len(templates)
            mad_libs(templates[pick])
        # retry the same game
        elif can_retry and text == "r": mad_libs(templates[pick])
        # exit
        elif text == "e": return
        else: print("\nInvalid input")

if __name__ == "__main__": main()

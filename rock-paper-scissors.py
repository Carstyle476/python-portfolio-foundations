
from random import randint

def main() -> None:
    # list of options
    options: list[str] = [
        "rock",
        "paper",
        "scissors",
        "Spock",
        "lizard"
    ]
    option_count: int = len(options)

    # results and messages for every pairing
    results: list[list[tuple[int, str]]] = [
        [
            (0,  "ties"),
            (-1, "gets wrapped by"),
            (1,  "crushes"),
            (-1, "gets vaporized by"),
            (1,  "crushes")
        ],
        [
            (1,  "wraps"),
            (0,  "ties"),
            (-1, "gets cut by"),
            (1,  "orders"),
            (-1, "gets stolen by")
        ],
        [
            (-1, "gets crushed by"),
            (1,  "cuts"),
            (0,  "ties"),
            (-1, "gets vaporized by"),
            (1,  "cuts")
        ],
        [
            (1,  "vaporizes"),
            (-1, "gets ordered by"),
            (1,  "vaporizes"),
            (0,  "talks with parallel universe"),
            (-1, "gets scared of")
        ],
        [
            (-1, "gets crushed by"),
            (1,  "steals"),
            (-1, "gets cut by"),
            (1,  "scares"),
            (0,  "ties")
        ]
    ]

    # display the list of options
    display: str = "\n"
    for i in range(option_count): display += f"{i} - {options[i]}\n"

    # score tracking
    player: int = 0
    cpu:    int = 0

    # game loop
    while True:
        # formatting
        print()

        text: str            = input(f"{display}\nYour score: {player}\nCPU's score: {cpu}\nSelect an option (blank to exit)\n>>> ")
        player_selected: int = -1
        valid: bool          = False

        # only accept proper input
        if text.isnumeric():
            player_selected = int(text)
            if player_selected < option_count: valid = True
        elif text == "": return
        
        if valid:
            # determine who won
            cpu_selected: int             = randint(0, option_count - 1)
            result:       tuple[int, str] = results[player_selected][cpu_selected]
            if result[0] == 1:  player += 1
            if result[0] == -1: cpu += 1

            print(f"\n{options[player_selected].capitalize()} {result[1]} {options[cpu_selected]}!")
        else: print("\nInvalid input")

if __name__ == "__main__": main()

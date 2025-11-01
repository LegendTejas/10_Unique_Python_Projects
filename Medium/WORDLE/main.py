import wordle
import os

# Clear terminal
os.system("cls" if os.name == "nt" else "clear")

# --- Show Game Instructions ---
instructions = [
    "----------------------------------------------",
    "                 HOW TO PLAY                  ",
    "----------------------------------------------",
    "• Guess the WORDLE in 6 tries",
    "• Each guess must be a valid 5-letter word",
    "• After each guess, the color of the letters will show how close your guess was",
    "",
    "Color Meaning:",
    "GREEN  - Letter is in the word and in the correct spot",
    "YELLOW - Letter is in the word but in the wrong spot",
    "GRAY   - Letter is not in the word",
    "",
    "Type 'h' anytime to view keyboard status",
    "----------------------------------------------",
]
print("\n".join(instructions))
input("\nPress Enter to begin...")

# Clear again before game starts
os.system("cls" if os.name == "nt" else "clear")

# --- Begin Banner ---
begin_message = """
'##:::::'##::'#######::'########::'########::'##:::::::'########:
 ##:'##: ##:'##.... ##: ##.... ##: ##.... ##: ##::::::: ##.....::
 ##: ##: ##: ##:::: ##: ##:::: ##: ##:::: ##: ##::::::: ##:::::::
 ##: ##: ##: ##:::: ##: ########:: ##:::: ##: ##::::::: ######:::
 ##: ##: ##: ##:::: ##: ##.. ##::: ##:::: ##: ##::::::: ##...::::
 ##: ##: ##: ##:::: ##: ##::. ##:: ##:::: ##: ##::::::: ##:::::::
. ###. ###::. #######:: ##:::. ##: ########:: ########: ########:
:...::...::::.......:::..:::::..::........:::........::........::
"""

print(begin_message.replace("#", f"{wordle.Color.YELLOW}#{wordle.Color.BASE}"))

# --- Main Game Loop ---
if __name__ == '__main__':
    with open("cheat.txt", "w") as f:
        f.write(wordle.CHOSEN_WORD)

    while True:
        guess = wordle.GuessWord(
            w_str=input(f"[{wordle.GuessWord.counter}]> ")
        )

        if guess.w_str == "h":
            list_values = list(wordle.GuessWord.alphabet.values())
            for element in list_values:
                print(
                    element,
                    end=" " if list_values[-1] != element else "\n"
                )
            continue

        if guess.is_valid():
            guess.apply_guesses()
            guess.check_perfect_guess()
            guess.jump_turn()
            guess.check_game_loss()
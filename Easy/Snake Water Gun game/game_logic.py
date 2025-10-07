import random

# Choice mapping
choices = {"Snake": 1, "Water": -1, "Gun": 0}
reverse = {1: "Snake", -1: "Water", 0: "Gun"}

def play_game(user_choice):
    """Returns computer choice and result"""
    comp = random.choice([-1, 0, 1])
    comp_choice = reverse[comp]
    you = choices[user_choice]

    if comp == you:
        result = "😑 It's a Draw!"
    elif (you == 1 and comp == -1) or (you == 0 and comp == 1) or (you == -1 and comp == 0):
        result = "˘⌣˘ You Win!"
    else:
        result = "💻 You Lose!"

    return comp_choice, result
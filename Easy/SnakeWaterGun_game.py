import tkinter as tk
import random

# Choice mapping
choices = {"Snake": 1, "Water": -1, "Gun": 0}
reverse = {1: "Snake", -1: "Water", 0: "Gun"}

def play(user_choice):
    comp = random.choice([-1, 0, 1])
    comp_choice = reverse[comp]
    you = choices[user_choice]

    if comp == you:
        result = "😑 It's a Draw!"
    elif (you == 1 and comp == -1) or (you == 0 and comp == 1) or (you == -1 and comp == 0):
        result = "˘⌣˘ You Win!"
    else:
        result = "💻 You Lose!"

    lbl_user.config(text=f"You chose: {user_choice}")
    lbl_comp.config(text=f"Computer chose: {comp_choice}")
    lbl_result.config(text=result)

# Main window
root = tk.Tk()
root.title("Snake Water Gun Game")
root.geometry("480x420")
root.config(bg="#d6f5f5")

# Title
tk.Label(root, text="🐍 Snake • 💧 Water • 🔫 Gun", font=("Arial", 18, "bold"), bg="#d6f5f5", fg="#004d40").pack(pady=20)
tk.Label(root, text="Choose your move:", font=("Arial", 13), bg="#d6f5f5").pack(pady=10)

# Buttons frame
frame = tk.Frame(root, bg="#d6f5f5")
frame.pack(pady=20)

tk.Button(frame, text="🐍 Snake", font=("Arial", 12, "bold"), width=10, bg="#aed581",
          command=lambda: play("Snake")).grid(row=0, column=0, padx=12, pady=8)
tk.Button(frame, text="💧 Water", font=("Arial", 12, "bold"), width=10, bg="#81d4fa",
          command=lambda: play("Water")).grid(row=0, column=1, padx=12, pady=8)
tk.Button(frame, text="🔫 Gun", font=("Arial", 12, "bold"), width=10, bg="#ffab91",
          command=lambda: play("Gun")).grid(row=0, column=2, padx=12, pady=8)

# Result labels
lbl_user = tk.Label(root, text="", font=("Arial", 12), bg="#d6f5f5")
lbl_user.pack(pady=5)

lbl_comp = tk.Label(root, text="", font=("Arial", 12), bg="#d6f5f5")
lbl_comp.pack(pady=5)

lbl_result = tk.Label(root, text="", font=("Arial", 15, "bold"), bg="#d6f5f5", fg="#004d40")
lbl_result.pack(pady=15)

# Exit button
tk.Button(root, text="Exit Game", font=("Arial", 12, "bold"), bg="#ef5350", fg="white",
          width=12, command=root.destroy).pack(pady=10)

root.mainloop()

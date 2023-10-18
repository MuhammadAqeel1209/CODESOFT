from tkinter import *
import random

user_score = 0
computer_score = 0

def play_game(user_choice):
    global user_score, computer_score

    choices = {"Rock": 0, "Paper": 1, "Scissors": 2}
    user_choice_index = choices[user_choice]

    computer_choice_index = random.randint(0, 2)
    computer_choices = list(choices.keys())
    computer_choice = computer_choices[computer_choice_index]

    result = determine_winner(user_choice_index, computer_choice_index)

    if result == "User wins":
        user_score += 1
    elif result == "Computer wins":
        computer_score += 1

    score_label.config(text=f"User: {user_score} | Computer: {computer_score}")
    result_label.config(text=f"User chose {user_choice}\nComputer chose {computer_choice}\n{result}")

def determine_winner(user_choice_index, computer_choice_index):
    if user_choice_index == computer_choice_index:
        return "It's a tie"
    if (user_choice_index - computer_choice_index) % 3 == 1:
        return "User wins"
    return "Computer wins"

def reset_scores():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    score_label.config(text="User: 0 | Computer: 0",font="Algerain 12")
    result_label.config(text="")

root = Tk()
root.title("Rock, Paper, Scissors Game")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()


root.geometry(f"{screen_width}x{screen_height}")
label = Label(text="Rock Paper Scissor Game",font="Algerain 26 bold",bg="Blue")
label.pack(padx=10,pady=20)

choices_frame = Frame(root)
choices_frame.pack(pady=20)
rock_button = Button(choices_frame, text="Rock", font=("Algerain", 12),command=lambda: play_game("Rock"),bg="red")
paper_button = Button(choices_frame, text="Paper",font=("Algerain", 12), command=lambda: play_game("Paper"),bg="red")
scissors_button = Button(choices_frame, text="Scissors",font=("Algerain", 12), command=lambda: play_game("Scissors"),bg="red")
rock_button.pack(side= LEFT, padx=10)
paper_button.pack(side= LEFT, padx=10)
scissors_button.pack(side= LEFT, padx=10)

result_label = Label(root, text="", font=("Algerain", 14))
result_label.pack(pady=20)
score_label = Label(root, text="User: 0 | Computer: 0", font=("Algerain", 12),bg ="red")
score_label.pack()

reset_button = Button(root, text="Play Again",font=("Algerain", 12),bg="red", command=reset_scores)
reset_button.pack(pady=20)

root.mainloop()
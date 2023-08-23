import random

choices = ["rock", "paper", "scissors"]

user_choice = input("Choose rock, paper, or scissors: ")
computer_choice = random.choice(choices)

print(f"Computer chose {computer_choice}")

if user_choice == computer_choice:
    result = "It's a tie!"
elif user_choice == "rock":
    result = "You win!" if computer_choice == "scissors" else "Computer wins!"
elif user_choice == "paper":
    result = "You win!" if computer_choice == "rock" else "Computer wins!"
elif user_choice == "scissors":
    result = "You win!" if computer_choice == "paper" else "Computer wins!"
else:
    result = "Invalid choice. Please choose rock, paper, or scissors."

print(result)

import random
import time

print("Let's play Rock, Paper, Scissors!")

# keep track of scores
user_score = 0
computer_score = 0
ties = 0

while True:
    user_choice = input("Choose rock, paper, scissors, or quit: ").lower()

    # quit game
    if user_choice == "quit":
        print("Thanks for playing!")
        break

    # check if user input can be accepted
    if user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice! Please enter rock, paper, or scissors")
        continue

    # computer chooses
    print("Computer's turn...")
    time.sleep(2)

    computer_choice = random.choice(["rock", "paper", "scissors"])

    print("You chose:", user_choice)
    print("Computer chose:", computer_choice)

    # determine the winner
    if user_choice == computer_choice:
        ties += 1
        print("It's a tie! 😲")

    elif user_choice == "rock" and computer_choice == "scissors":
        print("You won! 😄")
    elif user_choice == "paper" and computer_choice == "rock":
        print("You won! 😄")
    elif user_choice == "scissors" and computer_choice == "paper":
        print("You won! 😄")
    else:
        user_score += 1
        print("Computer won! 😔")

    # ask if player wants to play again
    play_again = input("Would you like to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("Thanks for playing!")
        break
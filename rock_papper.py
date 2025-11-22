import random

print("===== ROCK • PAPER • SCISSORS =====")
print("Instructions: Type rock, paper, or scissors to play!\n")

# Score tracking
user_score = 0
computer_score = 0

while True:
    # User Input
    user_choice = input("Enter your choice (rock/paper/scissors): ").lower()

    # Validate input
    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice! Please try again.\n")
        continue

    # Computer Selection
    computer_choice = random.choice(["rock", "paper", "scissors"])
    
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    # Game Logic
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        result = "You win!"
        user_score += 1
    else:
        result = "You lose!"
        computer_score += 1

    # Display the result
    print(result)
    print(f"Score → You: {user_score} | Computer: {computer_score}\n")

    # Ask if the user wants to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    print()

    if play_again != "yes":
        print("Thanks for playing! Final Score:")
        print(f"You: {user_score} | Computer: {computer_score}")
        print("Goodbye!")
        break

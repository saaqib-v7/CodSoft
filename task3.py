import random

def game(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (
        (user == "rock" and computer == "scissors") or
        (user == "scissors" and computer == "paper") or
        (user == "paper" and computer == "rock")
    ):
        return "You win!"
    else:
        return "You lose!"

def play():
    options = ["rock", "paper", "scissors"]

    while True:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice in options:
            break
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")

    computer_choice = random.choice(options)

    result = game(user_choice, computer_choice)

    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    print(result)

    return result

def main():
    user_score = 0
    computer_score = 0

    while True:
        result = play()

        if "win" in result:
            user_score += 1
        elif "lose" in result:
            computer_score += 1

        print(f"\nScores - You: {user_score}, Computer: {computer_score}")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    main()

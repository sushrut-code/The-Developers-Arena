import random

# Initial Setup
print("Hi, what is your Name??")
name = input("Name: ")
print(f"Hello, {name}! Guess a number between 1 to 100.\n"
      "You get 5 chances per round. If you guess it right, you get 1 point.\n"
      "If you lose, you lose a point, but your score can never go below zero.")
start = input("Are you ready to Play?? (y/n): ")
score = 0

while start.lower() == "y":
    # 1. Game Setup for the round
    my_number = random.randint(1, 100)


    win = 0  # Initialize win status for the round

    # 2. Guessing Loop
    for chance in range(1, 6):  # Loop 5 times (1 to 5)
        print(f"Chance {chance}/5")

        # Input validation (Optional, but good practice)
        while True:
            try:
                user_input = int(input("Write your number: "))
                if 1 <= user_input <= 100:
                    break
                else:
                    print("Please enter a number between 1 and 100.")
            except ValueError:
                print("Invalid input. Please enter a whole number.")

        if user_input == my_number:
            win = 1
            print("\nHurray! You guessed it right.")
            break  # Exit the guessing loop immediately

        elif user_input < my_number:
            print("You guessed a number less than what is desired.")

        else:
            print("You guessed a number bigger than what is desired.")

    # 3. Score Calculation (Outside the guessing loop)
    if win == 1:
        score += 1
        print(f"Current Score: +1 point.")
    else:
        score -= 1
        print(f"Current Score: -1 point. The correct number was {my_number}.")

    # Logic to prevent score from dropping below zero
    if score < 0:
        score = 0
        print("Your score cannot go below zero. Score capped at 0.")

    # 4. Display and Continue Prompt
    print(f"\nYour total score is {score}.")

    # Check if the player wants to continue
    start = input("Do you want to continue playing?? (y/n): ")

# Final Goodbye Message
if score > 0:
    print(f"\nGame Over! Your final score is {score}. Great job, {name}!")
else:
    print("\nGame Over! Your final score is zero, but nice try.")
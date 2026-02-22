# Number Guessing Game

import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100...")
    
    secret_number = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            guess = int(input("Make a guess: "))
            attempts += 1
            
            if guess < secret_number:
                print("Too low! Try again.🔽")
            elif guess > secret_number:
                print("Too high! Try again.🔼")
            else:
                print(f"Congratulations! 🎉 You guessed the number {secret_number} in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number!")

if __name__ == "__main__":
    number_guessing_game()

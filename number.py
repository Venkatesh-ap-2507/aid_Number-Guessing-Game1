import random

def play_again():
    play_again = input("Do you want to play again? (yes/no): ")
    return play_again.lower() == "yes"

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    name = input("What is your name? ")
    print(f"Hello, {name}!")
    print("I'm thinking of a number between 1 and 100.")
    secret_number = random.randint(1, 100)

    attempts = 0
    while attempts < 10:
        guess = int(input("Take a guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"Congratulations, {name}! You guessed the number in {attempts} attempts!")
            if play_again():
                number_guessing_game()
            else:
                print("Thank you for playing. Goodbye!")
                return

    print(f"Game over! You ran out of attempts. The number was {secret_number}.")
    if play_again():
        number_guessing_game()
    else:
        print("Thank you for playing. Goodbye!")

number_guessing_game()

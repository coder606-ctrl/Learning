import random

print("Welcome to the Number Guesser!")
print("I'm thinking of a number between 1 and 100.")
print("Try to guess it in as few attempts as possible.")
print("Type 0 to quit.\n")


def number_guesser():
    secN = random.randint(1, 100)
    attempts = 0
    print(secN) # Debugging line
    while True:
        try:
            guess = int(input("Enter your guess: "))

            if guess == 0:
                print("Thanks for playing!")
                break

            attempts += 1

            if guess < secN:
                print("Too low! Try again.")
            elif guess > secN:
                print("Too high! Try again.")

            elif guess == secN and attempts == 1:
                print(f"Congratulations! You guessed the number in {attempts} attempt.")
                again = input("Do you want to play again? (yes/no): ").strip()

                if again in ["no", "No", "NO", "n", "N"]:
                    print("Thanks for playing!")
                    break
                elif again in ["yes", "Yes", "YES", "y", "Y"]:
                    secN = random.randint(1, 100)
                    print(secN) # Debugging line
                    attempts = 0
                    continue
            elif guess == secN and attempts > 1:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                
                again = input("Do you want to play again? (yes/no): ").strip()

                if again in ["no", "No", "NO", "n", "N"]:
                    print("Thanks for playing!")
                    break
                elif again in ["yes", "Yes", "YES", "y", "Y"]:
                    secN = random.randint(1, 100)
                    print(secN) # Debugging line
                    attempts = 0
                    continue
                else:
                    print("Invalid input. Exiting program...")
                    break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    number_guesser()

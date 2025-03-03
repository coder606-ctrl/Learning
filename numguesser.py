import random

def numGuesser():
    secNum = random.randint(1, 100)
    
    print("Welcome to the Number Guesser Game!")
    print("I have selected a number between 1 and 100.")
    print("Try to guess the number in as few attempts as possible.")
    
    while True:
        try:
            guess = int(input("Enter your guess or type 0 to exit: "))

            if guess == 0:
                print("Goodbye!")
                break
            elif guess < secNum:
                print("Higher!")
            elif guess > secNum:
                print("Lower!")
            else:
                print("Congratulations! You guessed the number!")
                
                again = input("Would you like to play again? (y/n): ")
                if again.lower() in ['y', 'yes']:
                    secNum = random.randint(1, 100)
                    print("I have selected a number between 1 and 100.")
                    print("Try to guess the number in as few attempts as possible.")
                elif again.lower() in ['n', 'no']:
                    print("Goodbye!")
                    break
                else:
                    print("Invalid input. Goodbye.")
                    break

        except ValueError:
            print("Invalid input. Please enter a number between 1 and 100.")

numGuesser()
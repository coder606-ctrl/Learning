import random

wordlist = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon", "mango", "nectarine", "orange", "pear", "quince", "raspberry", "strawberry", "tangerine", "ugli", "watermelon", "xigua", "yellow", "zucchini"]

def wordGuesser():
    word = random.choice(wordlist)
    
    print("Welcome to the Word Guesser Game!")
    print("I have selected a word from the dictionary.")
    print("Try to guess the word in as few attempts as possible.")
    print(", ".join(wordlist))
    print("What you see above is the word list, try to guess the word in as few attempts as possible.")
    
    while True:
        try:
            guess = input("Enter your guess or type 'exit' to exit: ")

            if guess.lower() == 'exit':
                print("Goodbye!")
                break
            elif guess.lower() < word:
                print("Higher in the list!")
            elif guess.lower() > word:
                print("Lower in the list!")
            else:
                print("Congratulations! You guessed the word!")
                
                again = input("Would you like to play again? (y/n): ")
                if again.lower() in ['y', 'yes']:
                    word = random.choice(wordlist)
                    print("I have selected a word from the dictionary.")
                    print("Try to guess the word in as few attempts as possible.")
                elif again.lower() in ['n', 'no']:
                    print("Goodbye!")
                    break
        except ValueError:
            print("Invalid input. Please enter a word from the dictionary.")

wordGuesser()
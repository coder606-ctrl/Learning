from dictionary import capitals
# IMPORTANT, MAKE SURE TO ALSO USE THE DICTIONARY.PY FILE FOR THIS PROGRAMME, IT WON'T WORK OTHERWISE. YOU COULD ALSO MAKE YOUR OWN.

continents = [
    "Asia",
    "Africa",
    "North America",
    "South America",
    "Europe",
    "Antarctica",
    "Oceania",
]


def capitalteller():
    print("Welcome to the Capital Teller!")
    print("I can tell you the capital of almost any country in the world.")
    print("Type 'exit' to quit.")
    while True:
        country = input("Enter a country: ")
        if country in ['exit', 'quit']:
            break
        if country in capitals:
            print(f"The capital of {country} is {capitals[country]}.")
        elif country in continents:
            print(f"{country} is a continent. Please enter a country.")
            break
        else:
            print("I'm sorry, I don't know the capital of that country. Try respelling it, if it still doesn't work I don't know the capital.")
    print("Goodbye!")

capitalteller()

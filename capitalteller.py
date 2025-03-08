from dictionary import capitals

continents = [
    "Asia",
    "Africa",
    "Europe",
    "North America",
    "South America",
    "Australia",
    "Antarctica"
]

print("Welcome to the Capital Teller!")
print("I can tell you the capital of any country in the world.")
print("Type exit to quit the program.\n")

def capital_teller():
    while True:
        try:
            country = input("Enter the name of a country: ")

            if country == "exit":
                print("Thanks for using the Capital Teller!")
                break

            if country in capitals:
                print(f"The capital of {country} is {capitals[country]}.")

                again = input("Do you want to know the capital of another country? (y/n): ")

                if again in ["y", "Y", "yes", "Yes", "YES"]:
                    continue
                elif again in ["n", "N", "no", "No", "NO"]:
                    print("Thanks for using the Capital Teller!")
                    break
                else:
                    print("Invalid input. Please enter y or n.")

            elif country in continents:
                print(f"{country} is a continent, not a country. Please enter a valid country name.")
            else:
                print(f"Sorry, I don't know the capital of {country}. Try respelling it or check if it exists.")
        except KeyboardInterrupt:
            print("\nProgram ended. Thanks for using the Capital Teller!")
            break

if __name__ == "__main__":
    capital_teller()
            
                

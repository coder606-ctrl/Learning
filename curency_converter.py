from currency import exchange_rates

def currency_converter():  

    print("Available currencies:")
    print("1. USD - US Dollar")
    print("2. EUR - Euro")
    print("3. GBP - British Pound")
    print("4. JPY - Japanese Yen")
    print("5. AUD - Australian Dollar")
    print("6. CAD - Canadian Dollar")
    print("7. CHF - Swiss Franc")
    print("8. CNY - Chinese Yuan")
    print("9. SEK - Swedish Krona")
    print("10. NZD - New Zealand Dollar")
    print("11. MXN - Mexican Peso")
    print("12. SGD - Singapore Dollar")
    print("13. HKD - Hong Kong Dollar")
    print("14. NOK - Norwegian Krone")
    print("15. KRW - South Korean Won")
    print("16. RUB - Russian Ruble")
    print("17. INR - Indian Rupee")
    print("18. BRL - Brazilian Real")

    currency_dict = {
        "1": "USD",
        "2": "EUR",
        "3": "GBP",
        "4": "JPY",
        "5": "AUD",
        "6": "CAD",
        "7": "CHF",
        "8": "CNY",
        "9": "SEK",
        "10": "NZD",
        "11": "MXN",
        "12": "SGD",
        "13": "HKD",
        "14": "NOK",
        "15": "KRW",
        "16": "RUB",
        "17": "INR",
        "18": "BRL",
    }


    currency_from = input("Enter the currency you want to convert from. This is also the currency you will be entering your amount in. (1-18): ")
    if currency_from in ['exit', 'Exit', 'EXIT']:
        print("Goodbye!")
        return
    
    currency_to = input("Enter the currency you want to convert to (1-18): ")

    if currency_to in ['exit', 'Exit', 'EXIT']:
        print("Goodbye!")
        return
        
    currency_from_code = currency_dict.get(currency_from)
    currency_to_code = currency_dict.get(currency_to)

    if currency_from_code and currency_to_code:
        try:
            amount = float(input("Enter the amount to convert: "))
            if amount < 0:
                print("Please enter a positive amount.")
                return

            # Use the correct conversion formula
            rate_from = exchange_rates[currency_from_code]
            rate_to = exchange_rates[currency_to_code]
            converted_amount = amount * (rate_to / rate_from)  # Correct ratio for conversion

            print(f"{amount} {currency_from_code} is equal to {converted_amount:.2f} {currency_to_code}")

            again = input("Would you like to convert another currency? (y/n): ")

            if again in ["y", "Y", "yes", "Yes", "YES"]:
                currency_converter()
            elif again in ["n", "N", "no", "No", "NO"]:
                print("Goodbye!")
                return
            else:
                print("Invalid input. Please enter y or n.")

        except ValueError:
            print("Please enter a valid number for the amount.")
    else:
        print("Invalid currency selection.")

if __name__ == "__main__":
    currency_converter()

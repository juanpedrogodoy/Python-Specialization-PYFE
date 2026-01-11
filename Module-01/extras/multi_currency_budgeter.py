# Multi-Currency Travel Budgeter
# Exercise asked to the IA like a final boss!
# This script manages a travel budget by converting different currencies (EUR, GBP, MXN) to USD and tracking the total expenses.
# It uses functions, loops, and try/except for robust user input.

total = 0.0

def convert_to_usd(amount, currency):
    if currency == "EUR":
        return amount * 1.10
    elif currency == "GBP":
        return amount * 1.25
    elif currency == "MXN":
        return amount * 0.05
    elif currency == "USD":
        return amount * 1
    else:
        return 0

while True:
    article = input("Name of article: ")
    if article == "done":
        break
        
    currency = input("Please insert the currency code (USD, EUR, GBP, MXN): ").upper()
    amount = input("Please insert the amount: ")
    
    try:
        amount = float(amount)
    except:
        print("Input not valid")
        continue
        
    convert = convert_to_usd(amount, currency)
    total = total + convert
    
if total > 500:
    print("Budget limit of U$S 500 exceeded")
    print("Total: ", total)
else:
    print("The result is: ", total)

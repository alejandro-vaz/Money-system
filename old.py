import math
import os
import time
import json
from datetime import datetime

# FUNCTIONS
def invest_calc(n):
    # Calculate the invest_calc value based on the logarithm of n.
    n = math.log10(n)
    if n < 0:
        return 1
    if 0 <= n < 6:
        return 1 - 0.125 * n
    if 6 <= n < 7:
        return 0.25 - 0.2 * (n - 6)
    return 0.05

def spendable_calc(n):
    # Calculate the spendable_calc value based on the logarithm of n.
    n = math.log10(n)
    if n < 0:
        return 0
    if 0 <= n < 2:
        return 0.125 * n
    if 2 <= n < 3:
        return 0.25 - 0.15 * (n - 2)
    if 3 <= n < 5:
        return 0.1 + 0.05 * (n - 3)
    if 5 <= n < 8:
        return 0.2 - 0.05 * (n - 5)
    return 0.05

def lifestyle_calc(n):
    # Calculate the lifestyle_calc value based on the logarithm of n.
    n = math.log10(n)
    if n < 2:
        return 0
    if 2 <= n < 3:
        return 0.275 * (n - 2)
    if 3 <= n < 4:
        return 0.275 + 0.075 * (n - 3)
    if 4 <= n < 5:
        return 0.35 - 0.15 * (n - 4)
    if 5 <= n < 7:
        return 0.2
    if 7 <= n < 8:
        return 0.2 - 0.05 * (n - 7)
    if 8 <= n < 9:
        return 0.15 - 0.1 * (n - 8)
    return 0.05

def mp_calc(n):
    # Calculate the mp_calc value based on the logarithm of n.
    n = math.log10(n)
    if n < 4:
        return 0
    if 4 <= n < 5:
        return 0.225 * (n - 4)
    if 5 <= n < 6:
        return 0.225 + 0.175 * (n - 5)
    if 6 <= n < 7:
        return 0.4 + 0.25 * (n - 6)
    if 7 <= n < 9:
        return 0.65 + 0.1 * (n - 7)
    return 0.85

def calculate_all(total, net):
    # Calculate all account values based on total and net amount.
    return (
        invest_calc(total) * net,
        spendable_calc(total) * net,
        lifestyle_calc(total) * net,
        mp_calc(total) * net
    )

def apx(value, channel):
    # Round the value based on the specified channel.
    return math.floor(value * 100) / 100 if channel == 0 else math.ceil(value * 100) / 100

def liststrtofloat(lst):
    # Convert a list of strings to a list of floats.
    return [float(i) for i in lst]

def sumoflist(lst):
    # Return the sum of a list.# 
    return sum(lst)

def calculate(tax_rate, amount, total_accounts):
    # Calculate the financial breakdown based on tax rate and amount.
    tax = apx(tax_rate * amount, 1)
    usable = amount - tax
    invest, spendable, lifestyle, ms = calculate_all(total_accounts + amount, usable)
    return [
        spendable,
        lifestyle,
        invest,
        ms / 2,
        ms / 2,
        tax
    ]

def load_accounts(filename):
    # Load account values from a file, creating it if it doesn't exist.
    try:
        with open(filename, "r") as file:
            accounts = file.read().split("a")
    except FileNotFoundError:
        with open(filename, "x") as file:
            file.write("0a0a0a0a0a0")
            accounts = ["0", "0", "0", "0", "0", "0"]
    return liststrtofloat(accounts)

def save_accounts(filename, accounts):
    # Save account values to a file.
    with open(filename, "w") as file:
        file.write("a".join(map(lambda x: f"{round(x, 2):.2f}", accounts)))

def log_transaction(amount, metadata, description):
    transaction = {
        "amount": amount,
        "metadata": metadata,
        "date": datetime.now().strftime("%d/%m/%Y-%H:%M:%S"),
        "description": description
    }
    # Open the JSON file in read mode to load existing data
    try:
        with open("transactions.json", 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []  # If the file doesn't exist, start with an empty list
    except json.JSONDecodeError:
        data = []  # If the file is empty or corrupted, start with an empty list

    # Append the new dictionary to the list
    data.append(transaction)

    # Write the updated list back to the JSON file
    with open("transactions.json", 'w') as file:
        json.dump(data, file, indent=4)

def get_target_account(answer, accounts):
    # Get the target account based on user input.
    target = ""
    while target not in ["spendable", "lifestyle", "invest", "system", "peace", "tax", "general"]:
        target = input("Which account was the one targeted? ").lower()
        if target in ["spendable", "lifestyle", "invest", "system", "peace", "tax"]:
            index = ["spendable", "lifestyle", "invest", "system", "peace", "tax"].index(target)
            accounts[index] += answer
        elif target == "general":
            return target
        else:
            print("Invalid input")
    return target

def main():
    def show_accounts():
        print("ACCOUNTS:")
        print("==========================")
        print(f"spendable: {round(accounts[0], 2):.2f}")
        print(f"lifestyle: {round(accounts[1], 2):.2f}")
        print(f"invest: {round(accounts[2], 2):.2f}")
        print(f"system: {round(accounts[3], 2):.2f}")
        print(f"peace: {round(accounts[4], 2):.2f}")
        print(f"tax: {round(accounts[5], 2):.2f}")
        print("==========================")

    # Main function to run the money system.
    print("Welcome to the accounts system!")
    print("==========================")
    time.sleep(2)
    os.system("cls")
    accounts = load_accounts("accounts.line")
    show_accounts()
    print("")
    
    while True:
        answer = input("Enter command: ")
        try:
            answer = float(answer)
        except:
            answer = answer.lower()
            if answer == "exit":
                break
            if answer == "reset":
                if input("Are you sure you want to reset your account values? (y/n) ") == "y":
                    accounts = [0, 0, 0, 0, 0, 0]
                    try:
                        os.remove("transactions.json")
                    except:
                        pass
            if answer == "values":
                tax_rate = float(input("Enter the tax rate: "))
        else:
            if answer == 0:
                pass
            if answer < 0:
                target = get_target_account(answer, accounts)
                log_transaction(answer, target, input("Enter transaction description (5 to 50 words): "))
            if answer > 0:
                target = get_target_account(answer, accounts)
                if target == "general":
                    tax_rate = float(input("Enter the tax rate: "))
                    results = calculate(tax_rate, answer, sumoflist(accounts))
                    for i in range(len(accounts)):
                        accounts[i] += results[i]
                    log_transaction(answer, results, input("Enter transaction description (5 to 50 words): "))
                else:
                    log_transaction(answer, target, input("Enter transaction description (5 to 50 words): "))
        os.system("cls")
        if (answer == "reset") or (type(answer) == float) or (answer == "balances"):
            show_accounts()
        if answer == "help":
            print("COMMANDS:")
            print("==========================")
            print("reset - reset your account values")
            print("help - view this message")
            print("exit - exit the program")
            print("balances - view the breakdown of all accounts")
            print("(float) - add or substract money from accounts")
            print("values - view the breakdown of a single unit of money on your accounts")
        if answer == "values":
            print("VALUES:")
            print("==========================")
            print(calculate(tax_rate, 1, sumoflist(accounts)))
        print("")

        # OVERWRITE
        save_accounts("accounts.line", accounts)

if __name__ == "__main__":
    main()
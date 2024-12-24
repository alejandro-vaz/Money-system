import os
import system
import code
import menu
import handler
import sys
from datetime import datetime
import json

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def act(string, accs, trans, ass, sets, pas):
    def extract():
        print("Importing JSON...")
        import json
        print('Creating "transactions.json"...')
        open("transactions.json", "x")
        print('Creating "assets.json"...')
        open("assets.json", "x")
        print('Creating "user.txt"...')
        open("user.txt", "x")
        print('Creating "password.txt"...')
        open("password.txt", "x")
        print("Dumping transactions...")
        with open("transactions.json", "w") as file:
            json.dump(trans, file, indent=4)
        print("Dumping assets...")
        with open("assets.json", "w") as file:
            json.dump(ass, file, indent=4)
        print("Dumping user...")
        with open("user.txt", "w") as file:
            file.write(f"""{":".join(system.listfloattostr(accs))}
{":".join(system.listfloattostr(sets))}""")
        print("Dumping password...")
        with open("password.txt", "w") as file:
            file.write(pas)
        print("Extraction complete.")
    inp = string.split(" ")[0]
    args = string.split(" ")[1:]
    if (inp == "balance") or (inp == "balances"):
        money = system.sumoflist(accs)
        content = f"""
    Your total balance is {money}
"""
        return content, "BALANCE"
    if (inp == "exit") or (inp == "quit"):
        os.system("clear")
        exit(0)
    if (inp == "reset"):
        cwdir = str(os.getcwd())
        os.chdir(cwdir)
        os.remove("./data/user.txt.enc")
        os.remove("./data/transactions.json.enc")
        os.remove("./data/assets.json.enc")
        file_path = f"{cwdir.strip()}/start.py"
        os.system("clear")
        if "-exit" not in args:
            os.execv(sys.executable, [sys.executable, file_path])
        exit(0)
    if (inp == "help") or (inp == "?"):
        content = f"""
    account / shows accounts balance breakdown
    accounts / shows accounts balance breakdown
    admin / gives access to python interactive console
    balance / show your total balance across all accounts
    balances / show your total balance across all accounts
    breakdown / see the unit breakdown in your accounts
    exit / exits the program
    help / shows this help menu
    log / adds a positive transaction
        -general / uses custom automatic algorithm
        -invest / adds money into invest account
        -lifestyle / adds money into lifestyle account
        -peace / adds money into peace account
        -spendable / adds money into spendable account
        -system / adds money into system account
        -tax / adds money into tax account
    quit / exits the program
    reset / factory resets and restarts the program
        -exit / doesn't restart the program
    restart / restarts the program
    tax / shows the tax rate
        -change / changes the tax rate
    values / see the unit breakdown in your accounts
    ? / shows this help menu
"""
        return content, "COMMANDS"
    if (inp == "restart"):
        cwdir = str(os.getcwd())
        file_path = f"{cwdir.strip()}/start.py"
        os.system("clear")
        os.execv(sys.executable, [sys.executable, file_path])
    if (inp == "admin"):
        content = f"""
    Enter your password: """
        if menu.ask(content, "CYAN") == pas:
            os.system("clear")
            code.interact(local={**locals()}, banner="""You have flashed the memory. 
There's no turning back to the app unless you restart. 
You can use locals() to access all the variables or recall specific ones.
You can also use extract() to extract all the data.\n""")
        else:
            content = """
    Incorrect password
"""
            return content, "ERROR"
    if (inp == "tax"):
        if "-change" in args:
            content = f"""
    Enter the tax rate decimal float: """
            try:
                sets[0] = float(menu.ask(content, "CYAN"))
            except:
                return """
    Input is not a float or integer
""", "ERROR"
            data = f"""{":".join(system.listfloattostr(accs))}
{":".join(system.listfloattostr(sets))}"""
            handler.encrypt(data, pas, "./data/user.txt.enc")
            return f"""
    The tax rate was changed to {f"{100*sets[0]:.2f}%"}
""", "TAX RATE CHANGED"
        else:
            content = f"""
    The current tax rate is {f"{100*sets[0]:.2f}%"}
"""
            return content, "TAX RATE"
    if (inp == "log"):
        arguments = len(args)
        for i in args:
            if i not in ["-invest", "-lifestyle", "-peace", "-spendable", "-system", "-tax", "-general"]:
                return """
    Invalid argument
""", "ERROR"
        if len(args) == 0:
            return """
    You must provide at least one account as destination
""", "ERROR"
        content = f"""
    Enter the amount: """
        try:
            amount = float(menu.ask(content, "CYAN"))
        except:
            return """
    Input is not a float or integer
""", "ERROR"
        if "-invest" in args:
            accs[0] += amount / arguments * args.count("-invest")
        if "-lifestyle" in args:
            accs[1] += amount / arguments * args.count("-lifestyle")
        if "-peace" in args:
            accs[2] += amount / arguments * args.count("-peace")
        if "-spendable" in args:
            accs[3] += amount / arguments * args.count("-spendable")
        if "-system" in args:
            accs[4] += amount / arguments * args.count("-system")
        if "-tax" in args:
            accs[5] += amount / arguments * args.count("-tax")
        if "-general" in args:
            delta = system.divide_list(system.calculate(sets[0], amount, accs), arguments / args.count("-general"))
            accs = system.sum_lists(accs, delta)
        data = f"""{":".join(system.listfloattostr(accs))}
{":".join(system.listfloattostr(sets))}"""
        content = """
    Enter the description: """
        desc = menu.ask(content, "CYAN")
        transaction = {
            "amount": amount,
            "details": args,
            "delta": delta if "-general" in args else None,
            "time": datetime.now().strftime("%d/%m/%Y-%H:%M:%S"),
            "description": desc
        }
        trans.append(transaction)
        info = json.dumps(trans, indent=4)
        handler.encrypt(info, pas, "./data/transactions.json.enc")
        handler.encrypt(data, pas, "./data/user.txt.enc")
    if (inp == "accounts") or (inp == "account"):
        content = f"""
    # INVEST        {accs[0]:.2f}{" "*(12-len(f"{accs[0]:.2f}"))}({accs[0]})
    # LIFESTYLE     {accs[1]:.2f}{" "*(12-len(f"{accs[1]:.2f}"))}({accs[1]})
    # PEACE         {accs[2]:.2f}{" "*(12-len(f"{accs[2]:.2f}"))}({accs[2]})
    # SPENDABLE     {accs[3]:.2f}{" "*(12-len(f"{accs[3]:.2f}"))}({accs[3]})
    # SYSTEM        {accs[4]:.2f}{" "*(12-len(f"{accs[4]:.2f}"))}({accs[4]})
    # TAX           {accs[5]:.2f}{" "*(12-len(f"{accs[5]:.2f}"))}({accs[5]})
"""
        return content, "ACCOUNTS"
    if (inp == "values") or (inp == "breakdown"):
        return f"""
    Breakdown of 1: [{system.calculate(sets[0], 1, accs)}]
    """, "UNIT BREAKDOWN"
    return "", "MONEY SYSTEM"
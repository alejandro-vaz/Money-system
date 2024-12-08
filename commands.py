import os
import system
import code
import menu
import handler
import sys

def act(string, accs, trans, ass, sets, pas):
    inp = string.split(" ")[0]
    args = string.split(" ")[1:]
    
    if (inp == "balance") or (inp == "balances"):
        money = system.sumoflist(accs)
        content = f"""
    Your total balance is {money}
"""
        return content
    if (inp == "exit") or (inp == "quit"):
        os.system("cls")
        exit(0)
    if (inp == "reset"):
        cwdir = str(os.getcwd())
        os.chdir(cwdir)
        os.remove("./data/user.txt.enc")
        os.remove("./data/transactions.json.enc")
        os.remove("./data/assets.json.enc")
        file_path = f"{cwdir.strip()}\\start.py"
        os.system("cls")
        if "-exit" not in args:
            os.execv(sys.executable, ["python", f"\"{file_path}\""])
        exit(0)
    if (inp == "help") or (inp == "?"):
        content = f"""
    accounts / shows accounts balance breakdown
    admin / gives access to python console
    balance / show your total balance across all accounts
    balances / show your total balance across all accounts
    exit / exits the program
    help / shows this help menu
    income / adds a positive transaction
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
    ? / shows this help menu
"""
        return content
    if (inp == "restart"):
        cwdir = str(os.getcwd())
        file_path = f"{cwdir.strip()}\\start.py"
        os.system("cls")
        os.execv(sys.executable, ["python", f"\"{file_path}\""])
    if (inp == "admin"):
        content = f"""
    Enter your password: """
        if menu.ask(content, "CYAN") == pas:
            os.system("cls")
            code.interact(local={**locals(), **globals()}, banner="""You have flashed the memory. 
There's no turning back to the app unless you restart. 
You can use locals() and globals() to access all the variables or recall specific ones.\n""")
    if (inp == "tax"):
        if "-change" in args:
            content = f"""
    Enter the tax rate float: """
            sets[0] = float(menu.ask(content, "CYAN"))
            data = f"""{":".join(system.listfloattostr(accs))}
{":".join(system.listfloattostr(sets))}"""
            handler.encrypt(data, pas, "./data/user.txt.enc")
            return f"""
    The tax rate was changed to {sets[0]}
"""
        else:
            content = f"""
    The current tax rate is {sets[0]}
"""
            return content
    if (inp == "income"):
        arguments = len(args)
        if len(args) == 0:
            return """
    You must provide at least one account as destination
"""
        content = f"""
    Enter the positive amount: """
        amount = float(menu.ask(content, "CYAN"))
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
        return content
    return ""
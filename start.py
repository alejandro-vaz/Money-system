import handler
import menu
import json
import commands
import system
import os

print("\033[?25l", end="")
os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.system("clear")
os.system("xdotool key F11")
os.system("autohotkey")

def load():
    accounts = handler.decrypt(password, "./data/user.txt.enc").splitlines()[0].split(":")
    settings = handler.decrypt(password, "./data/user.txt.enc").splitlines()[1].split(":")
    accounts = system.liststrtofloat(accounts)
    settings = system.liststrtofloat(settings)
    transactions = json.loads(handler.decrypt(password, "./data/transactions.json.enc"))
    assets = json.loads(handler.decrypt(password, "./data/assets.json.enc"))
    return accounts, settings, transactions, assets

if __name__ == "__main__":
    try:
        menu.start(2)
        password = menu.login()
        accounts, settings, transactions, assets = load()
    except:
        pass

result = ""
head = "MONEY SYSTEM"
while True:
    accounts, settings, transactions, assets = load()
    command = menu.main(result, head)
    result, head = commands.act(command, accounts, transactions, assets, settings, password)
import handler
import menu
import json
import commands
import system

if __name__ == "__main__":
    menu.start(2)
    try:
        password = menu.login()
        accounts = handler.decrypt(password, "./data/user.txt.enc").splitlines()[0].split(":")
        settings = handler.decrypt(password, "./data/user.txt.enc").splitlines()[1].split(":")
        accounts = system.liststrtofloat(accounts)
        settings = system.liststrtofloat(settings)
        transactions = json.loads(handler.decrypt(password, "./data/transactions.json.enc"))
        assets = json.loads(handler.decrypt(password, "./data/assets.json.enc"))
    except:
        try:
            password = menu.login()
            accounts = handler.decrypt(password, "./data/user.txt.enc").splitlines()[0].split(":")
            settings = handler.decrypt(password, "./data/user.txt.enc").splitlines()[1].split(":")
            accounts = system.liststrtofloat(accounts)
            settings = system.liststrtofloat(settings)
            transactions = json.loads(handler.decrypt(password, "./data/transactions.json.enc"))
            assets = json.loads(handler.decrypt(password, "./data/assets.json.enc"))
        except:
            try:
                password = menu.login()
                accounts = handler.decrypt(password, "./data/user.txt.enc").splitlines()[0].split(":")
                settings = handler.decrypt(password, "./data/user.txt.enc").splitlines()[1].split(":")
                accounts = system.liststrtofloat(accounts)
                settings = system.liststrtofloat(settings)
                transactions = json.loads(handler.decrypt(password, "./data/transactions.json.enc"))
                assets = json.loads(handler.decrypt(password, "./data/assets.json.enc"))
            except:
                exit(0)

def modify(target, value):
    if target == "accounts":
        accounts = value
    if target == "settings":
        settings = value
    if target == "transactions":
        transactions = value
    if target == "assets":
        assets = value
    if target == "password":
        password = value

result = ""
while True:
    accounts = handler.decrypt(password, "./data/user.txt.enc").splitlines()[0].split(":")
    settings = handler.decrypt(password, "./data/user.txt.enc").splitlines()[1].split(":")
    accounts = system.liststrtofloat(accounts)
    settings = system.liststrtofloat(settings)
    transactions = json.loads(handler.decrypt(password, "./data/transactions.json.enc"))
    assets = json.loads(handler.decrypt(password, "./data/assets.json.enc"))
    command = menu.main(result)
    result = commands.act(command, accounts, transactions, assets, settings, password)
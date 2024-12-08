from colorama import init, Fore, Style, Cursor
import os
import time
init(autoreset=True)

def say(text, color):
    color = color.upper()
    colors = {
        "RESET": Style.RESET_ALL,
        "BLACK": Fore.BLACK,
        "RED": Fore.RED,
        "GREEN": Fore.GREEN,
        "YELLOW": Fore.YELLOW,
        "CYAN": Fore.BLUE,
        "MAGENTA": Fore.MAGENTA,
        "CYAN": Fore.CYAN,
        "WHITE": Fore.WHITE
    }
    if color in colors:
        print(colors[color] + text + colors["RESET"])
    else:
        print(text)

def ask(question, color):
    color = color.upper()
    colors = {
        "RESET": Style.RESET_ALL,
        "BLACK": Fore.BLACK,
        "RED": Fore.RED,
        "GREEN": Fore.GREEN,
        "YELLOW": Fore.YELLOW,
        "CYAN": Fore.BLUE,
        "MAGENTA": Fore.MAGENTA,
        "CYAN": Fore.CYAN,
        "WHITE": Fore.WHITE
    }
    if color in colors:
        return input(colors[color] + question + colors["RESET"])
    else:
        return input(question)

def move(right, down):
    print(Cursor.POS(right, down), end="")

def start(duration):
    os.system("cls")
    content = f"""{"="*120}
    WELCOME
{"="*120}
    
    Loading Money System...
    
    """
    say(content, "CYAN")
    move(5, 7)
    time.sleep(duration)

def login():
    os.system("cls")
    content = f"""{"="*120}
    LOGIN
{"="*120}
    
    If it's your first time logging in the system, choose a password to encrypt the files.
    
    Enter your password: """
    
    return ask(content, "CYAN")

def main(show):
    os.system("cls")
    content = f"""{"="*120}
    MONEY SYSTEM
{"="*120}
    {show}
    > """
    
    return ask(content, "CYAN").lower()
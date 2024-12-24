from colorama import init, Fore, Style, Cursor
import os
import time


init(autoreset=True)
os.chdir(os.path.dirname(os.path.abspath(__file__)))

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
        "BLUE": Fore.BLUE,
        "MAGENTA": Fore.MAGENTA,
        "CYAN": Fore.CYAN,
        "WHITE": Fore.WHITE
    }
    if color in colors:
        return input(colors[color] + question + colors["RESET"])
    else:
        return input(question)

def start(duration):
    os.system("clear")
    content = f"""{"="*211}
    WELCOME
{"="*211}
    
    Loading Money System...
    
    """
    say(content, "CYAN")
    time.sleep(duration)

def login():
    os.system("clear")
    content = f"""{"="*211}
    LOGIN
{"="*211}
    
    If it's your first time logging in, choose a password to encrypt the files.
    
    Enter your password: """
    
    return ask(content, "CYAN")

def main(show, title):
    os.system("clear")
    content = f"""{"="*211}
    {title}
{"="*211}
    {show}
    > """
    
    return ask(content, "CYAN").lower()
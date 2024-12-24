import math
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def sumoflist(list):
    count = 0
    for i in list:
        count += i
    return count

def liststrtofloat(elements):
    new = []
    for i in range(len(elements)):
        new.append(float(elements[i]))
    return new

def listfloattostr(elements):
    new = []
    for i in range(len(elements)):
        new.append(str(elements[i]))
    return new

def calculate(tax_rate, amount, accounts):
    def calcprop_in(n):
        try:
            n = math.log10(n)
        except:
            return 1
        if n < 0:
            return 1
        if 0 <= n < 6:
            return 1 - 0.125 * n
        if 6 <= n < 7:
            return 0.25 - 0.2 * (n - 6)
        return 0.05

    def calcprop_sp(n):
        try:
            n = math.log10(n)
        except:
            return 0
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

    def calcprop_li(n):
        try:
            n = math.log10(n)
        except:
            return 0
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

    def calcprop_mp(n):
        try:
            n = math.log10(n)
        except:
            return 0
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
    
    if amount > 0:
        tax_money = tax_rate * amount
    else:
        tax_money = 0
    usable = amount - tax_money
    return [
        calcprop_in(sumoflist(accounts) + amount) * usable,
        calcprop_li(sumoflist(accounts) + amount) * usable,
        calcprop_mp(sumoflist(accounts) + amount) * usable / 2,
        calcprop_sp(sumoflist(accounts) + amount) * usable,
        calcprop_mp(sumoflist(accounts) + amount) * usable / 2,
        tax_money
    ]

def sum_lists(list_1, list_2):
    if not len(list_1) == len(list_2):
        raise Exception("Lists must be the same length")
    new = []
    for i in range(len(list_1)):
        new.append(list_1[i] + list_2[i])
    return new

def divide_list(list, n):
    new = []
    for i in range(len(list)):
        new.append(list[i] / n)
    return new

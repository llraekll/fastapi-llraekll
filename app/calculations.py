def add(num1: int, num2: int):
    return num1+num2

def subract(num1: int, num2: int):
    return num1-num2

def multiply(num1: int, num2: int):
    return num1*num2

def divide(num1: int, num2: int):
    return num1/num2

class Insufficientfunds(Exception):
    pass


class BankAccount():
    def __init__(self, starting_balance=0):
        self.balance = starting_balance

    def deposit(self,amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount> self.balance:
            raise Insufficientfunds("Insufficent funds")
        self.balance -= amount

    def collect_intrest(self):
        self.balance *= 1.1
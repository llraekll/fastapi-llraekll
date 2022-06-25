from app.calculations import add, subract, multiply, divide,BankAccount
import pytest

@pytest.mark.parametrize("num1, num2, expected", [
    (3,5,8),
    (15,16,31),
    (70,56,126)
])
def test_add(num1, num2, expected):
    assert add(num1, num2)==expected

def test_subract():
    assert subract(9,3)==6

def test_multiply():
    assert multiply(9,3)==27

def test_divide():
    assert divide(9,3)==3

def test_bank_set_initial_amount():
    bank_account = BankAccount(50)
    assert bank_account.balance == 50

def test_withdraw():
    bank_account =BankAccount(50)
    bank_account.withdraw(20)
    assert bank_account.balance == 30

def test_deposit():
    bank_account =BankAccount(50)
    bank_account.deposit(100)
    assert bank_account.balance == 150

def test_intrest():
    bank_account =BankAccount(100)
    bank_account.collect_intrest()
    assert bank_account.balance == 110.00000000000001
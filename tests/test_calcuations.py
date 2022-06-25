from app.calculations import add, subract, multiply, divide,BankAccount, Insufficientfunds
import pytest

@pytest.fixture
def zero():
    return BankAccount()

@pytest.fixture
def bank_account():
    return BankAccount(50)

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

def test_bank_set_initial_amount(bank_account):
    #bank_account = BankAccount(50)
    assert bank_account.balance == 50

def test_withdrawl(bank_account):
    bank_account.withdraw(20)
    assert bank_account.balance == 30

def test_deposit(zero):    
    zero.deposit(100)
    assert zero.balance == 100

def test_intrest(bank_account):
    bank_account.collect_intrest()
    assert round(bank_account.balance, 2) == 55

@pytest.mark.parametrize("deposited, withdraw, balance", [
    (70, 10, 60),
    (15, 12, 3),
    (69000, 757, 68243)
])
def test_transactions(zero, deposited, withdraw, balance):
    zero.deposit(deposited)
    zero.withdraw(withdraw)
    assert zero.balance == balance

def test_insufficient_funds(bank_account):
    with pytest.raises(Insufficientfunds):
        bank_account.withdraw(200)
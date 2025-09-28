import pytest
from bank_account import BankAccount

def test_bank_account_initial_balance():
    amount = BankAccount(1000)
    assert amount.get_balance() == 1000, '残高が正しくありません'

def test_deposit_positive_amount():
    amount = BankAccount(1000)
    amount.deposit(500)
    assert amount.get_balance() == 500, '預金残高が間違っています'

def test_withdraw_sufficient_blance():
    amount = BankAccount(1000)
    amount.withdraw(500)
    assert amount.get_balance() == 500, '引き出し後の残高が間違っています'

def test_withdraw_insufficient_blance():
    amount = BankAccount(1000)
    with pytest.raises(ValueError, match="残高不足です"):
        amount.withdraw(1500)

def test_withdraw_negative_amount():
    amount = BankAccount(1000)
    with pytest.raises(ValueError, match=r"^引き出し額は正の値でなければなりません$"):
        amount.withdraw(-100)

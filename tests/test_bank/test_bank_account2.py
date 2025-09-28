import pytest
from bank_account import BankAccount

@pytest.fixture
def initianl_amount():
    return BankAccount(1000)

def test_bank_account_initial_balance(initianl_amount):
    # amount = BankAccount(1000)
    assert initianl_amount.get_balance() == 1000, '残高が正しくありません'

def test_withdraw_sufficient_blance(initianl_amount):
    # amount = BankAccount(1000)
    initianl_amount.withdraw(500)
    assert initianl_amount.get_balance() == 500, '引き出し後の残高が間違っています'

def test_withdraw_negative_amount(initianl_amount):
    # amount = BankAccount(1000)
    with pytest.raises(ValueError, match=r"^引き出し額は正の値でなければなりません$"):
        initianl_amount.withdraw(-100)

def test_deposit_negative_amount(initianl_amount):
    # amount = BankAccount(1000)
    with pytest.raises(ValueError, match=r"^預金額は正の値でなければなりません$"):
        initianl_amount.deposit(-100)

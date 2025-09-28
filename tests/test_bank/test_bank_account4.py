import pytest
from bank_account import BankAccount

@pytest.mark.parametrize("initinal_amount, deposit_amount, expected_balance",[
    (0,1000,1000),(1000,1500,2500)
])

def test_deposit(initinal_amount, deposit_amount, expected_balance):
    amount = BankAccount(initinal_amount)
    assert amount.deposit(deposit_amount) == expected_balance, '残高計算が正しくありません'

# 正常な引き出しテスト
def test_withdraw():
    amount = BankAccount(2000)
    assert amount.withdraw(1500) == 500, '引き出し後の残高が正しくありません'

# 引き出し額が負の値の場合のテスト
def test_withdraw_negative_amount():
    amount = BankAccount(1000)
    with pytest.raises(ValueError, match="引き出し額は正の値でなければなりません"):
        amount.withdraw(-100)
# 引き出し額が0の場合のテスト
def test_withdraw_zero_amount():
    amount = BankAccount(1000)
    with pytest.raises(ValueError,match="引き出し額は正の値でなければなりません"):
        amount.withdraw(0)
#残高不足の場合のテスト
def test_withdraw_insufficient_balance():
    amount = amount = BankAccount(0)
    with pytest.raises(ValueError,match="残高不足です"):
        amount.withdraw(1000)

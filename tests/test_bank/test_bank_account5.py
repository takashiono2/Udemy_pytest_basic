import pytest
from bank_account import BankAccount

def test_withdraw_insufficient_balance():
    amount = BankAccount(500)
    with pytest.raises(ValueError,match="残高不足です"):
        amount.withdraw(501)

@pytest.mark.skip(reason="修正中です")
def test_deposit_positive_amount():
    amount = BankAccount(0)
    amount.deposit(500)
    assert amount.get_balance() == 500,"預金残高が間違っています"

    # 引き出し額が負の値の場合のテスト
def test_withdraw_negative_amount():
    amount = BankAccount(1000)
    with pytest.raises(ValueError, match="引き出し額は正の値でなければなりません"):
        amount.withdraw(-100)

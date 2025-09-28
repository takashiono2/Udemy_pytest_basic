import pytest
from bank_account import BankAccount

def test_get_balance_in_currency(mocker):
    # `bank_account`モジュール内の`requests.get`をモック
    mock_get = mocker.patch("bank_account.requests.get")

    # モックが返すオブジェクトを設定
    # `requests.get`は`status_code`と`json()`を持つレスポンスオブジェクトを返すので、
    # それを模倣するモックオブジェクトを作成
    mock_get.return_value = mocker.Mock(
        status_code=200,
        json=lambda: {'rate': 150} # json()メソッドが呼ばれたときに辞書を返すように設定
    )

    # テスト対象のメソッドを実行
    amount = BankAccount(1000)
    balance_JPY = amount.get_balance_in_currency("JPY")

    # 1. `requests.get`が正しいURLで呼び出されたことを確認
    mock_get.assert_called_once_with("https://fakecurrencyapi.com/?base=USD&currency=JPY")

    # 2. 通貨換算が正しく行われたことを確認
    assert balance_JPY == 150000, "変換後の値が正しくありません"
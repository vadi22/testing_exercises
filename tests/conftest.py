import pytest
import datetime
import decimal
from functions.level_1.four_bank_parser import SmsMessage, Expense, BankCard


@pytest.fixture
def today():
    return datetime.date.today()


@pytest.fixture
def tomorrow(today):
    return today + datetime.timedelta(days=1)


@pytest.fixture
def smsmessage():
    return SmsMessage(
        text='10 руб, 4588581647522006 10.01.23 12:10 11/12 authcode 1010',
        author='any_bank',
        sent_at=datetime.datetime(2023, 1, 10, 12, 10)
    )


@pytest.fixture
def bank_card():
    return BankCard(
        last_digits='2006',
        owner='any_name',
    )


@pytest.fixture
def bank_cards(bank_card):
    return [
        BankCard('3326', 'v_bank'),
        BankCard('3326', 'v_bank'),
        bank_card,
    ]


@pytest.fixture
def expense(bank_card):
    return Expense(
        amount=decimal.Decimal('10'),
        card=bank_card,
        spent_in='11/12',
        spent_at=datetime.datetime(2023, 1, 10, 12, 10),
    )

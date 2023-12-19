import datetime
import decimal
from typing import NamedTuple


class BankCard(NamedTuple):
    last_digits: str
    owner: str


class SmsMessage(NamedTuple):
    text: str
    author: str
    sent_at: datetime.datetime


class Expense(NamedTuple):
    amount: decimal.Decimal
    card: BankCard
    spent_in: str
    spent_at: datetime.datetime


def parse_ineco_expense(sms: SmsMessage, cards: list[BankCard]) -> Expense:
    raw_sum, raw_details = sms.text.split(', ')
    raw_details = raw_details.split(' authcode ')[0]
    raw_card, raw_date, raw_time, spend_in = raw_details.split(' ', maxsplit=3)
    return Expense(
        amount=decimal.Decimal(raw_sum.split(' ')[-2]),
        card=[c for c in cards if c.last_digits == raw_card[-4:]][0],
        spent_in=spend_in,
        spent_at=datetime.datetime.strptime(f'{raw_date} {raw_time}', '%d.%m.%y %H:%M'),
    )

# s = SmsMessage('1020 руб, 4400430255123326 20.02.23 16:20 7/11 authcode 3034', 'Jo', datetime.datetime(2000, 1, 2, 12, 13, 14))
# b = BankCard('3330', 'a_bank'), BankCard('3326', 'v_bank')
# print(parse_ineco_expense(s,b))
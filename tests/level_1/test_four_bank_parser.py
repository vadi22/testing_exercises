from functions.level_1.four_bank_parser import BankCard, SmsMessage, Expense, parse_ineco_expense


def test_parse_ineco_expense(smsmessage, bank_cards, expense):
    assert parse_ineco_expense(smsmessage, bank_cards) == expense

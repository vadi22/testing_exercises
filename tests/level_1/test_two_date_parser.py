from functions.level_1.two_date_parser import compose_datetime_from
import datetime


def test_compose_datetime_from_today(today):
    assert compose_datetime_from('today', '13 : 22') == datetime.datetime(
        today.year, today.month, today.day, 13, 22)


def test_compose_datetime_from_tomorrow(tomorrow):
    assert compose_datetime_from('tomorrow', '13 : 22') == datetime.datetime(
        tomorrow.year, tomorrow.month, tomorrow.day, 13, 22)

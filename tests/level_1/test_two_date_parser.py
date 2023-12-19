from functions.level_1.two_date_parser import compose_datetime_from
import pytest
import datetime

test_today = datetime.date.today()                                                                                         #Это плохо?
test_tomorrow = datetime.date.today() + datetime.timedelta(days=1)                                                
testdata = [
    ('today', '22:33', datetime.datetime(test_today.year, test_today.month, test_today.day, 22, 33)),
    ('tomorrow', '22:33', datetime.datetime(test_tomorrow.year, test_tomorrow.month, test_tomorrow.day, 22, 33)),
]

@pytest.mark.parametrize(
    'date_str, time_str, expected', testdata
)


def test_compose_datetime_from(date_str, time_str, expected):
    assert compose_datetime_from(date_str, time_str) == expected




def test_compose_datetime_from_today(today):
    assert compose_datetime_from('today', '13 : 22') == datetime.datetime(today.year, today.month, today.day, 13, 22)


def test_compose_datetime_from_tomorrow(tomorrow):
    assert compose_datetime_from('tomorrow', '13 : 22') == datetime.datetime(tomorrow.year, tomorrow.month, tomorrow.day, 13, 22)
from functions.level_1.five_title import change_copy_item

import pytest


@pytest.mark.parametrize(
    'title, max_main_item_title_length, expected',
    [
        ('str', 2, 'str'),
        ('string', 100, 'Copy of string'),
        ('Copy of str (5)', 100, 'Copy of str (6)'),
        ('Copy of str', 100,'Copy of str (2)'),
        ('(2)', 100, 'Copy of (2)'),
    ]
)

def test_change_copy_item(title, max_main_item_title_length, expected):
    assert change_copy_item(title, max_main_item_title_length) == expected

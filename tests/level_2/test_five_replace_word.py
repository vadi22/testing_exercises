from functions.level_2.five_replace_word import replace_word


import pytest


@pytest.mark.parametrize(
    'text, replace_from, replace_to, expected',
    [
        ('any text replace_from', 'replace_from', 'replace_to',
         'any text replace_to'),
    ]
)
def test_replace_word(text, replace_from, replace_to, expected):
    assert replace_word(text, replace_from, replace_to) == expected

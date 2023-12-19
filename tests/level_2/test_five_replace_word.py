from functions.level_2.five_replace_word import replace_word
import pytest

@pytest.mark.parametrize(
    'text, verb_female, gender, expected',
    [
        ('v_male', 'v_female', 'male', 'v_male'),
        ('v_male', 'v_female', 'female', 'v_female'),       
    ]
)
def test_genderalize(verb_male, verb_female, gender, expected):
    assert replace_word(verb_male, verb_female, gender) == expected
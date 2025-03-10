from functions.level_1.one_gender import genderalize
import pytest

@pytest.mark.parametrize(
    'verb_male, verb_female, gender, expected',
    [
        ('v_male', 'v_female', 'male', 'v_male'),
        ('v_male', 'v_female', 'female', 'v_female'),       
    ]
)
def test_genderalize(verb_male, verb_female, gender, expected):
    assert genderalize(verb_male, verb_female, gender) == expected


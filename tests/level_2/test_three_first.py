from functions.level_2.three_first import first, NOT_SET
import pytest


@pytest.mark.parametrize(
    'items, default, expected',
    [
        ([1, 2, 3], 'go', 1),
        ([], 1, None)

    ]

)
def test_first(items, default, expected):
    assert first(items, default) == expected


def test_exception_AttributeError():
    with pytest.raises(AttributeError):
        first([1, 2, 3], NOT_SET)

from functions.level_2.one_median import get_median_value
import pytest


@pytest.mark.parametrize(
        'items, expected',
        [
            ([1, 3, 2], 2),
            ([4, 3, 1, 2, 1], 2),
            ([4, 3, 1, 2], 2.5),
            ([], None)

        ]
)
def test_median_value_even(items, expected):
    assert get_median_value(items) == expected

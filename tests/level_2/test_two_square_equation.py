from functions.level_2.two_square_equation import solve_square_equation
import pytest


@pytest.mark.parametrize(
        'square_coefficient, linear_coefficient, const_coefficient, expected',
        [
            (1.0, 2.0, 3.0, (None, None)),
        ]
)
def test_square_equation_discriminant_minus(square_coefficient,
                                            linear_coefficient,
                                            const_coefficient,
                                            expected):
    assert solve_square_equation(square_coefficient,
                                 linear_coefficient,
                                 const_coefficient) == expected


@pytest.mark.parametrize(
        'square_coefficient, linear_coefficient, const_coefficient, expected',
        [
            (1.0, 4.0, 4.0, (-2.0, None)),
        ]
)
def test_square_equation_discriminant_null(square_coefficient,
                                           linear_coefficient,
                                           const_coefficient,
                                           expected):
    assert solve_square_equation(square_coefficient,
                                 linear_coefficient,
                                 const_coefficient) == expected


@pytest.mark.parametrize(
        'square_coefficient, linear_coefficient, const_coefficient, expected',
        [
            (1.0, -13.0, 12.0, (1.0, 12.0)),
        ]
)
def test_square_equation(square_coefficient,
                         linear_coefficient,
                         const_coefficient,
                         expected):
    assert solve_square_equation(square_coefficient,
                                 linear_coefficient,
                                 const_coefficient) == expected

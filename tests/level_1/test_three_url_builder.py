from functions.level_1.three_url_builder import build_url
import pytest

@pytest.mark.parametrize(
    'host_name, relative_url, get_params, expected',
    [
        (
            'www.domain.com', 'index.html',
            {'name1':'value1', 'name2':'value2'},
            'www.domain.com/index.html?name1=value1&name2=value2'
        ),
        ('www.domain.com', 'index.html', {}, 'www.domain.com/index.html'),
        ('www.domain.com', 'index.html', None, 'www.domain.com/index.html')
    ]
    )

def test_build_url(host_name, relative_url, get_params, expected):
    assert build_url(host_name, relative_url, get_params) == expected

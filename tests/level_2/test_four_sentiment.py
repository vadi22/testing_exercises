from functions.level_2.four_sentiment import check_tweet_sentiment
import pytest


@pytest.mark.parametrize(
    'text, good_words, bad_words, expected',
    [
        ('good_words bad_words bad_words', {'good_words'}, {'bad_words'},
         'BAD'
         ),
        ('good_words bad_words', {'good_words'}, {'bad_words'},
         None
         ),
        ('good_words bad_words good_words', {'good_words'}, {'bad_words'},
         'GOOD'
         ),
    ]
)
def test_check_tweet_sentiment(text, good_words, bad_words, expected):
    assert check_tweet_sentiment(text, good_words, bad_words) == expected

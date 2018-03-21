import pytest

from core.lang_processing.levenshtein import LevenshteinDistance


class TestLevenshteinDistance(object):
    @pytest.mark.parametrize('word_a, word_b, expected_distance', [
        ('a', '', 1),
        ('a', 'b', 2),
        ('hello', 'hll', 2),
        ('hello', 'hell', 1),
        ('hello', 'hallo', 2),
        ('london', 'on dont', 3),
        ('house', 'pause', 4),
    ])
    def test_distances(self, word_a, word_b, expected_distance):
        l = LevenshteinDistance()
        assert l.distance(word_a, word_b) == expected_distance

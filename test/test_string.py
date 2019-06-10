import pytest

import fun_string


class TestFunString:

    @pytest.mark.parametrize('word,first_unique', [
        ('mama', False),
        ('alele', 'a'),
        ('kajak', 'j'),
        ('eleloom', 'm')
    ])
    def test_first_unique_char(self, word, first_unique):
        assert fun_string.first_unique_char(word) == first_unique

    @pytest.mark.parametrize('astring,positions', [
        ('mama', [1, 3]),
        ('aantyapeaalaaa', [0, 1, 5, 8, 9, 11, 12, 13])
    ])
    def test_get_indices(self, astring, positions):
        assert fun_string.get_indices('a', astring) == positions

    @pytest.mark.parametrize('string,min_dist', [
        ('aabbccdd', 1),
        ('alejazda', 3),
        ('loremipsu', -1),
        ('kajak', 2),
    ])
    def test_repeated_min_distance(self, string, min_dist):
        assert fun_string.repeated_min_distance(string) == min_dist

    @pytest.mark.parametrize('first,second', [
        ('kajak', 'jakka'),
        ('a', 'a'),
        ('loremipsum', 'muspimerol')
    ])
    def test_is_permutation_positive(self, first, second):
        assert fun_string.is_permutation(first, second) is True
        assert fun_string.is_permutation(second, first) is True

    @pytest.mark.parametrize('first,second,failure_index', [
        ('lorem', 'loren', '4'),
        ('lorem', 'Lorem', '0'),
        ('randstring', 'stringdatr', '2'),
    ])
    def test_is_permutation_negative(self, first, second, failure_index):
        with pytest.raises(fun_string.NotPermutation) as e:
            fun_string.is_permutation(first, second)
        assert str(e.value) == failure_index
        with pytest.raises(fun_string.NotPermutation):
            fun_string.is_permutation(second, first)

    @pytest.mark.parametrize('permutationer,permutationee', [
        ('loremipsum', 'ipremlomus'),
        ('randloremtworand', 'rolem'),
        ('onetwothreefour', 'oufr'),
        ('onetwothreefour', 'owteon'),
    ])
    def test_contains_permutation_positive(self, permutationer, permutationee):
        assert fun_string.contains_permutation(permutationer, permutationee) > -1

    @pytest.mark.parametrize('permutationer,permutationee', [
        ('loremipsum', 'mipsuma'),
        ('loremipsum', 'plorem'),
        ('aaaalorem', 'aloamara'),
    ])
    def test_contains_permutation_negative(self, permutationer, permutationee):
        assert (
            fun_string.contains_permutation(permutationer, permutationee)
            ==
            -1
        )

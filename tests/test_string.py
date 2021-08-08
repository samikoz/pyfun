import pytest

from fun_string.find_unique_char import first_unique_char
from fun_string.repeated_min_distance import get_indices, repeated_min_distance
from fun_string.contains_permutation import is_permutation, NotPermutation, contains_permutation
from fun_string.squash_consecutive import squash_consecutive


class TestFirstUniqueChar:
    @pytest.mark.parametrize('word,first_unique', [
        ('mama', False),
        ('alele', 'a'),
        ('kajak', 'j'),
        ('eleloom', 'm')
    ])
    def test_first_unique_char(self, word, first_unique):
        assert first_unique_char(word) == first_unique


class TestRepeatedMinDistance:
    @pytest.mark.parametrize('astring,positions', [
        ('mama', [1, 3]),
        ('aantyapeaalaaa', [0, 1, 5, 8, 9, 11, 12, 13])
    ])
    def test_get_indices(self, astring, positions):
        assert get_indices('a', astring) == positions

    @pytest.mark.parametrize('string,min_dist', [
        ('aabbccdd', 1),
        ('alejazda', 3),
        ('loremipsu', -1),
        ('kajak', 2),
    ])
    def test_repeated_min_distance(self, string, min_dist):
        assert repeated_min_distance(string) == min_dist


class TestContainsPermutation:
    @pytest.mark.parametrize('first,second', [
        ('kajak', 'jakka'),
        ('a', 'a'),
        ('loremipsum', 'muspimerol')
    ])
    def test_is_permutation_positive(self, first, second):
        assert is_permutation(first, second) is True
        assert is_permutation(second, first) is True

    @pytest.mark.parametrize('first,second,failure_index', [
        ('lorem', 'loren', '4'),
        ('lorem', 'Lorem', '0'),
        ('randstring', 'stringdatr', '2'),
    ])
    def test_is_permutation_negative(self, first, second, failure_index):
        with pytest.raises(NotPermutation) as e:
            is_permutation(first, second)
        assert str(e.value) == failure_index
        with pytest.raises(NotPermutation):
            is_permutation(second, first)

    @pytest.mark.parametrize('permutationer,permutationee', [
        ('loremipsum', 'ipremlomus'),
        ('randloremtworand', 'rolem'),
        ('onetwothreefour', 'oufr'),
        ('onetwothreefour', 'owteon'),
    ])
    def test_contains_permutation_positive(self, permutationer, permutationee):
        assert contains_permutation(permutationer, permutationee) > -1

    @pytest.mark.parametrize('permutationer,permutationee', [
        ('loremipsum', 'mipsuma'),
        ('loremipsum', 'plorem'),
        ('aaaalorem', 'aloamara'),
    ])
    def test_contains_permutation_negative(self, permutationer, permutationee):
        assert (
            contains_permutation(permutationer, permutationee)
            ==
            -1
        )


class TestSquashConsecutive:
    def test_no_repetitions(self):
        assert squash_consecutive('abcd') == (('a', 1), ('b', 1), ('c', 1), ('d', 1))

    def test_non_repeated_repetitions(self):
        assert squash_consecutive('aabccdddd') == (('a', 2), ('b', 1), ('c', 2), ('d', 4))

    def test_repeated_repetitions(self):
        assert squash_consecutive('aabaaaca') == (('a', 2), ('b', 1), ('a', 3), ('c', 1), ('a', 1))

    def test_empty_string(self):
        assert squash_consecutive('') == ()

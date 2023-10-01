import pytest

from leetcode.problem_438 import Solution

test_data = [
    ("cbaebabacd", "abc", [0, 6]),
    ("abab", "ab", [0, 1, 2]),
    ("abab", "cd", []),
    ("a", "b", []),
    ("a", "a", [0]),
    ("aa", "a", [0, 1]),
]


@pytest.mark.parametrize("s, p, expected", test_data)
def test(s, p, expected):
    assert Solution().findAnagrams(s, p) == expected

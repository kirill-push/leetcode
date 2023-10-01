import pytest

from leetcode.problem_76 import Solution

test_data = [
    ("ADOBECODEBANC", "ABC", "BANC"),
    ("a", "a", "a"),
    ("a", "aa", ""),
    ("ab", "a", "a"),
    ("abc", "bc", "bc"),
    ("aa", "aa", "aa"),
    ("abc", "cba", "abc"),
]


@pytest.mark.parametrize("s, t, expected", test_data)
def test(s, t, expected):
    assert Solution().minWindow(s, t) == expected

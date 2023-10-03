import pytest

from leetcode.problem_5 import Solution

test_data = [
    ("babad", "bab"),
    ("cbbd", "bb"),
    ("a", "a"),
]


@pytest.mark.parametrize("s, expected", test_data)
def test(s, expected):
    assert Solution().longestPalindrome(s) == expected

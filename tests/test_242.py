import pytest

from leetcode.problem_242 import Solution

test_data = [
    ("anagram", "nagaram", True),
    ("rat", "car", False),
    ("a", "a", True),
    ("a", "b", False),
    ("aba", "aaab", False),
]


@pytest.mark.parametrize("s, t, expected", test_data)
def test(s, t, expected):
    assert Solution().isAnagram(s, t) == expected

import pytest

from leetcode.problem_3 import Solution

test_data = [
    ("abcabcbb", 3),
    ("bbbbb", 1),
    ("pwwkew", 3),
    ("aab", 2),
    ("", 0),
]


@pytest.mark.parametrize("s, expected", test_data)
def test(s, expected):
    assert Solution().lengthOfLongestSubstring(s) == expected

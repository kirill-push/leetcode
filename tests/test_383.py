import pytest

from leetcode.problem_383 import Solution

test_data = [
    ("a", "b", False),
    ("aa", "ab", False),
    ("aa", "aab", True),
    ("hello", "abchdrseeeeenltriuool", True),
    ("hello", "a", False),
]


@pytest.mark.parametrize("ransomNote, magazine, expected", test_data)
def test(ransomNote, magazine, expected):
    assert Solution().canConstruct(ransomNote, magazine) == expected

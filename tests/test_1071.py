import pytest

from leetcode.problem_1071 import Solution

test_data = [
    ("ABCABC", "ABC", "ABC"),
    ("ABABAB", "ABAB", "AB"),
    ("LEET", "CODE", ""),
]


@pytest.mark.parametrize("str1,str2,expected", test_data)
def test(str1, str2, expected):
    assert Solution().gcdOfStrings(str1, str2) == expected

import pytest

from leetcode.problem_125 import Solution

test_data = [
    ("A man, a plan, a canal: Panama", True),
    ("race a car", False),
    (" ", True),
    (".,", True),
    ("0P", False),
    ("000", True),
    ("001", False),
]


@pytest.mark.parametrize("s, expected", test_data)
def test(s, expected):
    assert Solution().isPalindrome(s) == expected

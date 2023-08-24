import pytest

from leetcode.problem_392 import Solution

test_data = [
    ("abc", "ahbgdc", True),
    ("axc", "ahbgdc", False),
]


@pytest.mark.parametrize("s,t,expected", test_data)
def test(s, t, expected):
    assert Solution().isSubsequence(s, t) == expected

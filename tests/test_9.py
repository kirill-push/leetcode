import pytest

from leetcode.problem_9 import Solution

test_data = [(121, True), (-121, False), (10, False), (0, True)]


@pytest.mark.parametrize("x, expected", test_data)
def test(x, expected):
    assert Solution().isPalindrome(x) == expected

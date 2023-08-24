import pytest

from leetcode.problem_1480 import Solution

test_data = [
    ([1, 2, 3, 4], [1, 3, 6, 10]),
    ([1, 1, 1, 1, 1], [1, 2, 3, 4, 5]),
    ([3, 1, 2, 10, 1], [3, 4, 6, 16, 17]),
]


@pytest.mark.parametrize("nums,expected", test_data)
def test(nums, expected):
    assert Solution().runningSum(nums) == expected

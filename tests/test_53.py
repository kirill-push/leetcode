import pytest

from leetcode.problem_53 import Solution

test_data = [
    ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
    ([1], 1),
    ([5, 4, -1, 7, 8], 23),
    ([-100], -100),
    ([-100, -1], -1),
    ([-100, -1, 1000, 0, 1], 1001),
    ([0], 0),
    ([-1, -2, -3, -1], -1),
]


@pytest.mark.parametrize("nums, expected", test_data)
def test(nums, expected):
    assert Solution().maxSubArray(nums) == expected

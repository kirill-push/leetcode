import pytest

from leetcode.problem_15 import Solution

test_data = [
    ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
    ([0, 1, 1], []),
    ([0, 0, 0], [[0, 0, 0]]),
    ([0, 0, 0, 0], [[0, 0, 0]]),
    ([-1, 0, 1, 0], [[-1, 0, 1]]),
    ([-2, -1, 0, 1, 1, 2], [[-2, 0, 2], [-2, 1, 1], [-1, 0, 1]]),
]


@pytest.mark.parametrize("nums, expected", test_data)
def test(nums, expected):
    assert Solution().threeSum(nums) == expected

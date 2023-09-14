import pytest

from leetcode.problem_1 import Solution

test_data = [
    ([2, 7, 11, 15], 9, [0, 1]),
    ([3, 2, 4], 6, [1, 2]),
    ([3, 3], 6, [0, 1]),
    ([0, 0], 0, [0, 1]),
    ([-2, -3, 0], -2, [0, 2]),
    ([-2, 3, 4, 5, 6, -100, 2], 0, [0, 6]),
]


@pytest.mark.parametrize("nums,target,expected", test_data)
def test(nums, target, expected):
    assert Solution().twoSum(nums, target) == expected

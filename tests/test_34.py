import pytest

from leetcode.problem_34 import Solution

test_data = [
    ([5, 7, 7, 8, 8, 10], 8, [3, 4]),
    ([5, 7, 7, 8, 8, 10], 6, [-1, -1]),
    ([], 0, [-1, -1]),
    ([0], 0, [0, 0]),
]


@pytest.mark.parametrize("nums,target,expected", test_data)
def test(nums, target, expected):
    assert Solution().searchRange(nums, target) == expected

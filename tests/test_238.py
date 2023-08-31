import pytest

from leetcode.problem_238 import Solution

test_data = [
    ([1, 2, 3, 4], [24, 12, 8, 6]),
    ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
    ([0, 0], [0, 0]),
    ([1, 1], [1, 1]),
    ([1, 2, 3, 4, 5], [120, 60, 40, 30, 24]),
    ([1, 2, 3, 4, 5, 6], [720, 360, 240, 180, 144, 120]),
    ([0, 0, 0, 0, 0], [0, 0, 0, 0, 0]),
]


@pytest.mark.parametrize("nums,expected", test_data)
def test(nums, expected):
    assert Solution().productExceptSelf(nums) == expected

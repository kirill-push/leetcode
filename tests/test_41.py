import pytest

from leetcode.problem_41 import Solution

test_data = [
    ([1, 2, 0], 3),
    ([3, 4, -1, 1], 2),
    ([7, 8, 9, 11, 12], 1),
    ([1], 2),
    ([2], 1),
]


@pytest.mark.parametrize("nums, expected", test_data)
def test(nums, expected):
    assert Solution().firstMissingPositive(nums) == expected

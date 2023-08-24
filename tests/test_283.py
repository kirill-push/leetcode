import pytest

from leetcode.problem_283 import Solution

test_data = [
    ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
    ([0], [0]),
]


@pytest.mark.parametrize("nums,expected", test_data)
def test(nums, expected):
    Solution().moveZeroes(nums)
    assert nums == expected

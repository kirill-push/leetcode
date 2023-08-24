import pytest

from leetcode.problem_724 import Solution

test_data = [
    ([1, 7, 3, 6, 5, 6], 3),
    ([1, 2, 3], -1),
    ([2, 1, -1], 0),
]


@pytest.mark.parametrize("nums,expected", test_data)
def test(nums, expected):
    assert Solution().pivotIndex(nums) == expected

import pytest

from leetcode.problem_152 import Solution

test_data = [
    ([2, 3, -2, 4], 6),
    ([-2, 0, -1], 0),
    ([0], 0),
    ([1], 1),
    ([0, -1], 0),
    ([0, 1, 0], 1),
]


@pytest.mark.parametrize("nums, expected", test_data)
def test(nums, expected):
    assert Solution().maxProduct(nums) == expected

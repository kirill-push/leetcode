import pytest

from leetcode.problem_239 import Solution

test_data = [
    ([1, 3, -1, -3, 5, 3, 6, 7], 3, [3, 3, 5, 5, 6, 7]),
    ([1], 1, [1]),
    ([1, 1, 2], 2, [1, 2]),
    ([1, 1, 2], 3, [2]),
]


@pytest.mark.parametrize("nums, k, expected", test_data)
def test(nums, k, expected):
    assert Solution().maxSlidingWindow(nums, k) == expected

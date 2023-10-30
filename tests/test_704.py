import pytest

from leetcode.problem_704 import Solution

test_data = [
    ([-1, 0, 3, 5, 9, 12], 9, 4),
    ([-1, 0, 3, 5, 9, 12], 2, -1),
    ([-1, 0, 3, 5, 9, 12], 13, -1),
]


@pytest.mark.parametrize("nums, target, expected", test_data)
def test(nums, target, expected):
    assert Solution().search(nums, target) == expected

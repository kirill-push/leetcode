import pytest

from leetcode.problem_209 import Solution

test_data = [
    (7, [2, 3, 1, 2, 4, 3], 2),
    (4, [1, 4, 4], 1),
    (11, [1, 1, 1, 1, 1, 1, 1, 1], 0),
    (1, [1], 1),
    (1, [2], 1),
    (2, [1], 0),
]


@pytest.mark.parametrize("target, nums, expected", test_data)
def test(target, nums, expected):
    assert Solution().minSubArrayLen(target, nums) == expected

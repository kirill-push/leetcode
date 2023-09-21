import pytest

from leetcode.problem_217 import Solution

test_data = [
    ([1, 2, 3, 1], True),
    ([1, 2, 3, 4], False),
    ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
    ([0], False),
    ([0, 0], True),
]


@pytest.mark.parametrize("nums, expected", test_data)
def test(nums, expected):
    assert Solution().containsDuplicate(nums) == expected

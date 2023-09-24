import pytest

from leetcode.problem_11 import Solution

test_data = [
    ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
    ([1, 1], 1),
    ([0, 0], 0),
    ([0, 10], 0),
    ([0, 10, 0], 0),
]


@pytest.mark.parametrize("height, expected", test_data)
def test(height, expected):
    assert Solution().maxArea(height) == expected

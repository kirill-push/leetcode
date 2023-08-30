import pytest

from leetcode.problem_274 import Solution

test_data = [
    ([3, 0, 6, 1, 5], 3),
    ([1, 3, 1], 1),
    ([0], 0),
    ([6], 1),
    ([1, 1, 1, 1, 1], 1),
]


@pytest.mark.parametrize("citations,expected", test_data)
def test(citations, expected):
    assert Solution().hIndex(citations) == expected

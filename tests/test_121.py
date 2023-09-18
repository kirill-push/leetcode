import pytest

from leetcode.problem_121 import Solution

test_data = [
    ([7, 1, 5, 3, 6, 4], 5),
    ([7, 6, 4, 3, 1], 0),
    ([0], 0),
    ([0, 0, 0], 0),
    ([100, 0, 0], 0),
    ([100, 0, 0, 1], 1),
]


@pytest.mark.parametrize("prices, expected", test_data)
def test(prices, expected):
    assert Solution().maxProfit(prices) == expected

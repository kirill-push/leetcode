import pytest

from leetcode.problem_88 import Solution

test_data = [
    ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
    ([1], 1, [], 0, [1]),
    ([0], 0, [1], 1, [1]),
    ([-100, -1, 0, 1, 0, 0], 4, [-1001, 100], 2, [-1001, -100, -1, 0, 1, 100]),
]


@pytest.mark.parametrize("nums1,m,nums2,n,expected", test_data)
def test(nums1, m, nums2, n, expected):
    Solution().merge(nums1, m, nums2, n)
    assert nums1 == expected

import pytest

from leetcode.problem_350 import Solution

test_data = [
    ([1, 2, 2, 1], [2, 2], [2, 2]),
    ([4, 9, 5], [9, 4, 9, 8, 4], [9, 4]),
    ([1, 2, 3], [5], []),
    ([1], [1], [1]),
]


@pytest.mark.parametrize("nums1,nums2,expected", test_data)
def test(nums1, nums2, expected):
    assert Solution().intersect(nums1, nums2).sort() == expected.sort()

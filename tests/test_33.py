import numpy as np
import pytest

from leetcode.problem_33 import Solution


def shifted_list(my_list, k):
    return my_list[k:] + my_list[:k]


def find_ans(my_list, ans):
    output = np.where(np.array(my_list) == ans)[0]
    if output.size > 0:
        return output.item()
    else:
        return -1


base_list = list(range(8))
test_data = [
    ([4, 5, 6, 7, 0, 1, 2], 0, 4),
    ([4, 5, 6, 7, 0, 1, 2], 3, -1),
    ([1], 0, -1),
] + [
    (shifted_list(base_list, i), j, find_ans(shifted_list(base_list, i), j))
    for i, j in zip([0, 0, 1, 1, 2, 2, 3, 3], [3, 100, 5, 10, 1, 20, 4, 55])
]


@pytest.mark.parametrize("nums,target,expected", test_data)
def test(nums, target, expected):
    assert Solution().search(nums, target) == expected

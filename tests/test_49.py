import pytest

from leetcode.problem_49 import Solution

test_data = [
    (
        ["eat", "tea", "tan", "ate", "nat", "bat"],
        [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
    ),
    ([""], [[""]]),
    (["a"], [["a"]]),
    (
        ["a", "", "", "a", "abc", "abb", "acb", ""],
        [["abc", "acb"], ["", "", ""], ["abb"], ["a", "a"]],
    ),
]


def sort_nested_lists(lst):
    return [sorted(sublist) for sublist in lst]


@pytest.mark.parametrize("strs, expected", test_data)
def test(strs, expected):
    assert sorted(sort_nested_lists(Solution().groupAnagrams(strs))) == sorted(
        sort_nested_lists(expected)
    )

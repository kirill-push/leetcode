import pytest

from leetcode.problem_424 import Solution

test_data = [
    ("ABAB", 2, 4),
    ("AABABBA", 1, 4),
    ("A", 1, 1),
    ("A", 0, 1),
    ("AB", 0, 1),
    ("ABBBBAABAABAA", 0, 4),
    ("ABCDEFFGZZAZDK", 4, 7),
]


@pytest.mark.parametrize("s, k, expected", test_data)
def test(s, k, expected):
    assert Solution().characterReplacement(s, k) == expected

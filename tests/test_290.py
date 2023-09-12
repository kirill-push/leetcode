import pytest

from leetcode.problem_290 import Solution

test_data = [
    ("abba", "dog cat cat dog", True),
    ("abba", "dog cat cat fish", False),
    ("aaaa", "dog cat cat dog", False),
    ("abba", "dog dog dog dog", False),
    ("a", "dog", True),
    ("aa", "dog cat", False),
    ("aaa", "dog cat cat dog", False),
    ("hc", "dog dog", False),
    ("hc", "cat dog", True),
]


@pytest.mark.parametrize("pattern,s,expected", test_data)
def test(pattern, s, expected):
    assert Solution().wordPattern(pattern, s) == expected

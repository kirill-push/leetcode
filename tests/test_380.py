import pytest

from leetcode.problem_380 import RandomizedSet

test_data = [
    (
        [
            "RandomizedSet",
            "insert",
            "remove",
            "insert",
            "getRandom",
            "remove",
            "insert",
            "getRandom",
        ],
        [[], [1], [2], [2], [], [1], [2], []],
        [None, True, False, True, 1, True, False, 2],
    ),
    (
        [
            "RandomizedSet",
            "remove",
            "remove",
            "insert",
            "getRandom",
            "remove",
            "insert",
        ],
        [[], [0], [0], [0], [], [0], [0]],
        [None, False, False, True, 0, True, True],
    ),
]


@pytest.mark.parametrize("method, val, expected", test_data)
def test(method, val, expected):
    ans = []
    for i, func in enumerate(method):
        if func == "RandomizedSet":
            my_set = RandomizedSet()
            ans.append(None)
        elif func == "insert":
            ans.append(my_set.insert(val[i][0]))
        elif func == "remove":
            ans.append(my_set.remove(val[i][0]))
        elif func == "getRandom":
            ans.append(my_set.getRandom())
    assert ans == expected

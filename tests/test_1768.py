import pytest

from leetcode.problem_1768 import Solution

test_data = [
    ("abc", "pqr", "apbqcr"),
    ("ab", "pqrs", "apbqrs"),
    ("abcd", "pq", "apbqcd"),
]

words = {"anmsdfjkhjlhs": 3, "uuududuu": 2, "ansdfuiyocvhn": 10, "acvcvdd": 1}


def base_words(ans, k1):
    word1 = []
    word2 = []

    k2 = len(ans) - k1
    k = min(k1, k2)
    for i, s in enumerate(ans):
        if i < 2 * k:
            if i % 2 == 0:
                word1.append(s)
            else:
                word2.append(s)
        elif k1 < k2:
            word2.append(s)
        else:
            word1.append(s)
    return ("".join(word1), "".join(word2), ans)


test_data_auto = [base_words(ans, words[ans]) for ans in words.keys()]


@pytest.mark.parametrize("word1,word2,expected", test_data)
def test(word1, word2, expected):
    assert Solution().mergeAlternately(word1, word2) == expected


@pytest.mark.parametrize("word1,word2,expected", test_data_auto)
def test_auto(word1, word2, expected):
    assert Solution().mergeAlternately(word1, word2) == expected

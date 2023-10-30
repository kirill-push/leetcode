import pytest

from leetcode.problem_22 import Solution

test_data = [
    (1, ["()"]),
    (2, ["(())", "()()"]),
    (3, ["((()))", "(()())", "(())()", "()(())", "()()()"]),
    (
        4,
        [
            "(((())))",
            "((()()))",
            "((())())",
            "((()))()",
            "(()(()))",
            "(()()())",
            "(()())()",
            "(())(())",
            "(())()()",
            "()((()))",
            "()(()())",
            "()(())()",
            "()()(())",
            "()()()()",
        ],
    ),
    (
        5,
        [
            "((((()))))",
            "(((()())))",
            "(((())()))",
            "(((()))())",
            "(((())))()",
            "((()(())))",
            "((()()()))",
            "((()())())",
            "((()()))()",
            "((())(()))",
            "((())()())",
            "((())())()",
            "((()))(())",
            "((()))()()",
            "(()((())))",
            "(()(()()))",
            "(()(())())",
            "(()(()))()",
            "(()()(()))",
            "(()()()())",
            "(()()())()",
            "(()())(())",
            "(()())()()",
            "(())((()))",
            "(())(()())",
            "(())(())()",
            "(())()(())",
            "(())()()()",
            "()(((())))",
            "()((()()))",
            "()((())())",
            "()((()))()",
            "()(()(()))",
            "()(()()())",
            "()(()())()",
            "()(())(())",
            "()(())()()",
            "()()((()))",
            "()()(()())",
            "()()(())()",
            "()()()(())",
            "()()()()()",
        ],
    ),
]


@pytest.mark.parametrize("n, expected", test_data)
def test(n, expected):
    assert sorted(Solution().generateParenthesis(n)) == sorted(expected)
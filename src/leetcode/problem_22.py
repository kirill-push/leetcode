from typing import List


class Solution:
    def _recursion(self, curr: str, left: int, right: int) -> None:
        if len(curr) == 2 * self.n:
            return self.ans.append(curr)

        if left < self.n:
            self._recursion(curr + "(", left + 1, right)

        if right < left:
            self._recursion(curr + ")", left, right + 1)

    def generateParenthesis(self, n: int) -> List[str]:
        self.n = n
        if n == 1:
            return ["()"]
        else:
            self.ans = []
            self._recursion("(", 1, 0)

            return self.ans

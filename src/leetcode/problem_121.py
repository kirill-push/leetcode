from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        ans = 0
        for el in prices[1:]:
            if el >= buy:
                ans = max(ans, el - buy)
            else:
                buy = el
        return ans

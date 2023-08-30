from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if len(citations) == 1:
            if citations[0] > 0:
                return 1
            else:
                return 0
        max_c = max(citations)
        counts = [0] * (max_c + 1)

        for c in citations:
            counts[c] += 1

        ans = 0
        for i, n in enumerate(counts[::-1]):
            c = max_c - i
            ans += n
            if ans >= c:
                return c
        return 1

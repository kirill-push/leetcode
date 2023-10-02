from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for word in strs:
            word_vec = [0] * 26
            for s in word:
                id_s = ord(s) - ord("a")
                word_vec[id_s] += 1
            tvec = tuple(word_vec)
            ans[tvec].append(word)
        return ans.values()

from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        ans = []
        hash_p = dict()
        for key in p:
            if key not in hash_p:
                hash_p[key] = 0
            hash_p[key] += 1
        for i, el in enumerate(s):
            if i < len(p) and el in hash_p:
                hash_p[el] -= 1
            elif i >= len(p):
                if el in hash_p:
                    hash_p[el] -= 1
                if s[i - len(p)] in hash_p:
                    hash_p[s[i - len(p)]] += 1
            if all(val == 0 for val in hash_p.values()):
                ans.append(i - len(p) + 1)
        return ans

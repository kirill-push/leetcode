from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hash_t = Counter(t)
        counts = len(t)
        left = 0
        min_len = len(s) + 1
        ans = [-1, 0]
        for right, key in enumerate(s):
            hash_t[key] -= 1
            if hash_t[key] >= 0:
                counts -= 1
            while counts == 0:
                if min_len > right - left + 1:
                    min_len = right - left + 1
                    ans = [left, right]
                hash_t[s[left]] += 1
                if hash_t[s[left]] > 0:
                    counts += 1
                left += 1
        if ans[0] == -1:
            return ""
        else:
            return s[ans[0] : ans[1] + 1]

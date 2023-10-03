class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = [0, 0]
        max_len = 1
        for i in range(1, len(s)):
            step = 0
            while (
                i - step >= 0
                and i + step < len(s)
                and s[i - step] == s[i + step]
            ):
                step += 1
            step -= 1
            if max_len < step * 2 + 1:
                max_len = step * 2 + 1
                ans = [i - step, i + step]
            step = 0
            while (
                i - 1 - step >= 0
                and i + step < len(s)
                and s[i - 1 - step] == s[i + step]
            ):
                step += 1
            step -= 1
            if max_len < (step + 1) * 2:
                max_len = (step + 1) * 2
                ans = [i - 1 - step, i + step]
        return s[ans[0] : ans[1] + 1]

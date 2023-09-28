class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        left = 0
        right = 1
        seen = {s[left]: left}
        ans = 1
        while right < len(s):
            if s[right] not in seen:
                ans = max(ans, right - left + 1)
            elif left <= seen[s[right]]:
                left = seen[s[right]] + 1
            else:
                ans = max(ans, right - left + 1)

            seen[s[right]] = right
            right += 1
        return ans

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 1
        ans = 1
        counter = {s[left]: 1}
        while right < len(s):
            if s[right] not in counter:
                counter[s[right]] = 0
            counter[s[right]] += 1

            current_len = right - left + 1
            max_count = max(counter.values())
            if current_len - max_count <= k:
                ans = max(ans, current_len)

            else:
                counter[s[left]] -= 1
                left += 1

            right += 1
        return ans

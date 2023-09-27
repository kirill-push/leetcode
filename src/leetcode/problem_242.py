class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        list_s = [0] * 26

        for i in range(len(s)):
            list_s[ord(s[i]) - ord("a")] += 1
            list_s[ord(t[i]) - ord("a")] -= 1

        return list_s == [0] * 26

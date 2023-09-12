class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        h_map = dict()

        if len(set(pattern)) != len(set(words)):
            return False
        if len(pattern) != len(words):
            return False

        for i, word in enumerate(words):
            if pattern[i] not in h_map:
                h_map[pattern[i]] = word
            if h_map[pattern[i]] != word:
                return False
        return True

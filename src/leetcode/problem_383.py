class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash_r = dict()
        for r in ransomNote:
            if r not in hash_r:
                hash_r[r] = 0
            hash_r[r] += 1
        for m in magazine:
            if m not in hash_r:
                continue
            hash_r[m] -= 1
            if hash_r[m] == 0:
                hash_r.pop(m)
            if not hash_r:
                return True
        return False

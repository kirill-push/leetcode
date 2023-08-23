class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        flag_1 = 0
        flag_2 = 0
        ans_arr = []
        end = False
        while not end:
            if flag_1 < len(word1):
                ans_arr.append(word1[flag_1])
                flag_1 += 1
            if flag_2 < len(word2):
                ans_arr.append(word2[flag_2])
                flag_2 += 1
            if flag_1 == len(word1) and flag_2 == len(word2):
                end = True
        return ''.join(ans_arr)

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [1]
        suff = [1]
        for i in range(len(nums) - 1):
            pref.append(nums[i] * pref[-1])
            suff.append(nums[-i - 1] * suff[-1])

        answer = []
        for i in range(len(nums)):
            answer.append(pref[i] * suff[-i - 1])
        return answer

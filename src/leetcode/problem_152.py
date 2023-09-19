from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        pref = 1
        suff = 1
        n = len(nums)

        ans = -float("inf")
        for i in range(len(nums)):
            pref *= nums[i]
            suff *= nums[n - i - 1]
            ans = max(ans, pref, suff)
            if pref == 0:
                pref = 1
            if suff == 0:
                suff = 1
        return ans

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        pref = [0]
        for n in nums:
            pref.append(pref[-1] + n)

        min_val = pref[0]
        ans = -float("inf")
        for i in range(1, len(pref)):
            min_val = min(min_val, pref[i - 1])
            ans = max(ans, pref[i] - min_val)

        return ans

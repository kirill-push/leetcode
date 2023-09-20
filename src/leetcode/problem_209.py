from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 1

        prefix = nums[0]
        if prefix >= target:
            return 1
        ans = len(nums) + 1

        while right < len(nums):
            prefix += nums[right]
            if prefix >= target:
                ans = min(ans, right - left + 1)
                prefix -= nums[left] + nums[right]
                left += 1
            else:
                right += 1
        if ans <= len(nums):
            return ans
        else:
            return 0

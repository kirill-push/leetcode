from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        summ = sum(nums)
        cum = 0
        for i in range(len(nums)):
            if (summ - nums[i]) % 2 == 0 and cum == (summ - nums[i]) // 2:
                return i
            cum += nums[i]
        return -1

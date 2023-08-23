from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        flag = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[flag] = nums[i]
                if flag < i:
                    nums[i] = 0
                flag += 1

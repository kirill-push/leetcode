from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i, n in enumerate(nums):
            if n < 0 or n > len(nums):
                nums[i] = 0

        for i, n in enumerate(nums):
            if n <= 0:
                continue
            else:
                if n == i + 1:
                    nums[i] = -1
                elif n > i + 1:
                    j = n - 1
                    nums[i] = 0
                    while nums[j] > 0:
                        curr_n = nums[j]
                        nums[j] = -1
                        j = curr_n - 1
                    nums[j] = -1
                else:
                    nums[n - 1] = -1
                    nums[i] = 0

        for i, n in enumerate(nums):
            if n >= 0:
                return i + 1
        return len(nums) + 1

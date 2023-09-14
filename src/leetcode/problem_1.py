from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = dict()
        for i in range(len(nums)):
            if nums[i] in table:
                return [table[nums[i]], i]
            table[target - nums[i]] = i

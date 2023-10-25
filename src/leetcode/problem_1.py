from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = dict()
        for i, n in enumerate(nums):
            if n in table:
                return [table[n], i]
            table[target - n] = i

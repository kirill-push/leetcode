from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 3:
            if sum(nums) == 0:
                return [nums]
            else:
                return []

        if len(set(nums)) == 1:
            if nums[0] == 0:
                return [[0, 0, 0]]
            else:
                return []

        ans = []
        left = 0
        right = len(nums) - 1

        nums.sort()

        for left in range(len(nums)):
            if left >= 1 and nums[left - 1] == nums[left]:
                continue
            middle = left + 1
            right = len(nums) - 1
            while middle < right:
                base = nums[middle] + nums[right] + nums[left]
                if base == 0:
                    ans.append([nums[left], nums[middle], nums[right]])
                    middle += 1
                    while nums[middle - 1] == nums[middle] and middle < right:
                        middle += 1
                elif base < 0:
                    middle += 1

                else:
                    right -= 1

        return ans

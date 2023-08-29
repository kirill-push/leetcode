from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]

        ans = []

        # starting position
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (right + left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] >= target:
                right = mid
        if nums[left] == target:
            ans.append(left)
        else:
            return [-1, -1]

        # ending position
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (right + left + 1) // 2
            if nums[mid] <= target:
                left = mid
            elif nums[mid] > target:
                right = mid - 1
        ans.append(left)

        return ans

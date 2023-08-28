from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while right >= left:
            m = (right + left) // 2
            if nums[m] == target:
                return m

            if nums[m] >= nums[left]:
                if nums[left] <= target and target < nums[m]:
                    right = m - 1
                else:
                    left = m + 1

            else:
                if nums[m] < target and target <= nums[right]:
                    left = m + 1
                else:
                    right = m - 1
        return -1

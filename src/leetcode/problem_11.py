from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        def water(left, right):
            return min(height[left], height[right]) * (right - left)

        U = water(left, right)

        while left < right:
            U = max(U, water(left, right))
            if height[left] >= height[right]:
                right -= 1
            else:
                left += 1
        return U

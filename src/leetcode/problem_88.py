from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        point1 = m - 1
        point2 = n - 1
        if n == 0:
            return None

        for i in range(1, n + m + 1):
            current = n + m - i
            if point1 >= 0 and point2 >= 0 and nums1[point1] >= nums2[point2]:
                nums1[current] = nums1[point1]
                point1 -= 1
                current -= 1
            elif point2 >= 0:
                nums1[current] = nums2[point2]
                point2 -= 1
                current -= 1
            else:
                return None

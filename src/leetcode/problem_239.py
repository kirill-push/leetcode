from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums

        if k == len(nums):
            return [max(nums)]

        queue = deque()

        ans = []

        for i, n in enumerate(nums):
            while len(queue) > 0 and nums[queue[-1]] <= n:
                queue.pop()

            queue.append(i)

            if queue[0] <= i - k:
                queue.popleft()

            if i >= k - 1:
                ans.append(nums[queue[0]])

        return ans

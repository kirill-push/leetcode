class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        left = 0
        right = len(x) - 1
        while right > left:
            if x[right] != x[left]:
                return False
            else:
                right -= 1
                left += 1
        return True

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""

        def my_gcd(i: int, j: int) -> int:
            if i == 0:
                return j
            else:
                return my_gcd(j % i, i)

        return str1[: my_gcd(len(str1), len(str2))]

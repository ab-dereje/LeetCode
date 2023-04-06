class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            result = int(str(x)[::-1])
        else:
            result = -int(str(abs(x))[::-1])

        if -2**31 <= result <= 2**31-1:
            return result
        else:
            return 0
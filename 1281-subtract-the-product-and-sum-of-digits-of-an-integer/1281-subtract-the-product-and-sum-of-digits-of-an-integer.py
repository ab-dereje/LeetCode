class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits = [int(digit) for digit in str(n)]
        product = 1
        for digit in digits:
            product *= digit
        digit_sum = sum(digits)
        result = product - digit_sum

        return result
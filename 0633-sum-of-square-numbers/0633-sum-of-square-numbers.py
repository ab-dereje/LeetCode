class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        b = int(sqrt(c))
        while b >= a:
            print(a,b)
            if (((a*a)+(b*b)) == c):
                return True
            if (((a*a)+(b*b)) > c):
                b -= 1
            if (((a*a)+(b*b)) < c):
                a += 1
        return False
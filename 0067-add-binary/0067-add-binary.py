class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a=int(f"{a}",2)
        b=int(f"{b}",2)
        c=a+b
        c=bin(c)
        c=c[2:]
        return c
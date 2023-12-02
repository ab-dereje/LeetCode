class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        a=str(n-1)
        b=str(1)
        for i in range(1,n):
            if(('0' in a) or ('0' in b)):
                a=int(a)-1
                b=int(b)+1
                a=str(a)
                b=str(b)
            else:
                return [int(a),int(b)]
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        g=[]
        l=["1","2","3","4","5","6","7","8","9"]
        c=0
        for i in range(left,right+1):
            j=str(i)
            for k in j:
                if ((k in l) and (int(j)%int(k)==0)):
                    c=1
                else:
                    c=0
                    break
            if (c==1):
                g.append(int(j))
                c=0
        return(g)
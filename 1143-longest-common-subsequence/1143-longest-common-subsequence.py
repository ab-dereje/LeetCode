class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        x=text1
        y=text2
        lx=len(x)
        ly=len(y)
        a=[[0 for i in range(lx+1)] for j in range(ly+1)]
        for j in range(1,ly+1):
            for i in range(1,lx+1):
                if(y[j-1]!=x[i-1]):
                    a[j][i]=max(a[j][i-1],a[j-1][i])
                else:
                    a[j][i]=a[j-1][i-1]+1
        return a[-1][-1]
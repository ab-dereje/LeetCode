class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        g=[]
        for i in accounts:
            a=sum(i)
            g.append(a)
            a=0
        return (max(g))
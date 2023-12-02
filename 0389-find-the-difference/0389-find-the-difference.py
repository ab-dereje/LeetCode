class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        checked=[]
        m=""
        for i in range(len(t)):
            if(t[i] not in checked):
                if(t.count(t[i])==s.count(t[i])):
                    checked.append(t[i])
                    continue
                else:
                    checked.append(t[i])
                    x=t.count(t[i])-s.count(t[i])
                    y=t[i]*x
                    m+=y
        return m
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        g=[]
        a=0
        h=[]
        for i in range(len(s)):
            for j in range(i,len(s)):
                if s[j] not in g:
                    g.append(s[j])
                    a+=1
                else:
                    break
            h.append(a)
            g=[]
            a=0
        if (len(h)>0):
            return (max(h))
        elif (len(s)>0):
            return 1
        else:
            return 0
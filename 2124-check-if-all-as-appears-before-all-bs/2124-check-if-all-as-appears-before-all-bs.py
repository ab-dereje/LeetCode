class Solution:
    def checkString(self, s: str) -> bool:
        cnt=0
        if ('b' in s ):
            x=s.index('b')
            if(x!=(len(s)-1)):
                for i in range(x+1,len(s)):
                    if(s[i]=='a'):
                        cnt+=1
        if('b' not in s):
            return True

        if(cnt==0):
            return True
        else:
            return False
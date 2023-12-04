class Solution:
    def numberOfSteps(self, num: int) -> int:
        a=0
        while num!=0:
            if (num%2==0):
                num=num//2
                a+=1
            else:
                num-=1
                a+=1
        return a
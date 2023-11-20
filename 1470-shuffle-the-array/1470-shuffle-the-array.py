class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        g=[]
        for i in range(n):
            g.append(nums[i])
            g.append(nums[i+n])
        return(g)
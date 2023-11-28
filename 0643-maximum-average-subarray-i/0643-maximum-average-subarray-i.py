class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        z=len(nums)
        a=sum(nums[:k])
        m=a
        for i in range(k,z):
            a=a+nums[i]-nums[i-k]
            m=max(m,a)
        return (m/k)
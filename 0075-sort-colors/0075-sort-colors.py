class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(1,len(nums)):
            for j in range(i):
                if(nums[i]<nums[j]):
                    nums[i],nums[j]=nums[j],nums[i]
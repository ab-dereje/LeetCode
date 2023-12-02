class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            for i in range (len(nums)):
                if(nums[i]>target):
                    return i
                if(i==len(nums)-1):
                    return i+1
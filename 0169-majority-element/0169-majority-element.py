class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        checker=[]
        for i in range( len(nums)):
            if(nums[i] in checker):
                continue
            else:
                if(nums.count(nums[i])>len(nums)/2):
                    return nums[i]
                else:
                    checker.append(nums[i])

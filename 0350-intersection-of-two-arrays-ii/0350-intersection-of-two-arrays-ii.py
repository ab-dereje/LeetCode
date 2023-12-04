from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter1 = Counter(nums1)
        counter2 = Counter(nums2)
        result = []

        for num in nums1:
            if num in counter2 and counter2[num] > 0:
                result.append(num)
                counter2[num] -= 1

        return result
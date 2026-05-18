'''class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen=set()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    return True
        else:
            return False

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen=set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
'''

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums))<len(nums):
            return True
        return False

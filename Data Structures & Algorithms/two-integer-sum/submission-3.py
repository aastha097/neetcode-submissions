class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i,num in enumerate(nums):
            seen[num]=i
        for i,num in enumerate(nums):
            diff=target-nums[i]
            if diff in seen and seen[diff]!=i:
                return [i,seen[diff]]
        return []

            

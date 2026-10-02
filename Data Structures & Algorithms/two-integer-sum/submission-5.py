class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i in range(0,len(nums)):
            complement=target-nums[i]
            if complement in seen:
                j=seen[complement]
                return [min(i,j),max(i,j)]
            seen[nums[i]]=i
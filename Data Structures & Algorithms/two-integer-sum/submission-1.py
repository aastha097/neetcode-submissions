'''class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if (nums[i]+nums[j]==target and i!=j):
                    result.append(min(i,j))
                    result.append(max(i,j))
                    return result

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        using hashmaps
        hashmap={}
        for i in range(len(nums)):
            complement=target-nums[i]
            if complement in hashmap:
                return [hashmap[complement],i]
            hashmap[nums[i]]=i
        return []'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices={}
        for i,n in enumerate(nums):
            indices[n]=i
        for i,n in enumerate(nums):
            diff=target-nums[i]
            if diff in indices and indices[diff]!=i:
                return[i,indices[diff]]
        return []
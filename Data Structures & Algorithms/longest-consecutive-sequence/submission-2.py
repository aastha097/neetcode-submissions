class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        myset=set(nums)
        ans=0
        for num in nums:
            if num-1 not in myset:
                start=num
                c=1
                while start+1 in myset:
                    c+=1
                    start+=1
                ans=max(ans,c)
        return ans
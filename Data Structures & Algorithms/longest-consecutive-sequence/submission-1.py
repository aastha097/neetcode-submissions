class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n=len(nums)
        seq=set(nums)
        ans=0
        for num in nums:
            if num-1 not in seq:
                start=num
                c=1
                while start+1 in seq:
                    c+=1
                    start+=1
                ans=max(c,ans)
                
        return ans


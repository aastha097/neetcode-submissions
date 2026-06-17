class Solution:
    def sumc(self,nums,ind,target,l,ans):
        if ind==len(nums):
            if target==0:
                ans.append(l.copy())
            return
        if nums[ind]<=target:
            l.append(nums[ind])
            self.sumc(nums,ind,target-nums[ind],l,ans)
            l.pop()
        self.sumc(nums,ind+1,target,l,ans)
        return ans
        
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        l=[]
        ans=[]
        return self.sumc(nums,0,target,l,ans)
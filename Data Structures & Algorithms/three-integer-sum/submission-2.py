class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()#in ascending ord
        count={}
        res=[]
        for i in range(len(nums)):
            val=nums[i]
            count[val]=count.get(val,0)+1# would result into {4:1,-1:2} {val:frequency}
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,len(nums)):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                req_k=-(nums[i]+nums[j])
                if req_k in count:
                    if req_k>nums[j]:
                        res.append([nums[i],nums[j],req_k])
                    elif req_k==nums[j]:
                        copies=2 if nums[i]==nums[j] else 1
                        if count[req_k]>=copies+1:
                            res.append([nums[i],nums[j],req_k])
                            break
        return res
                


        
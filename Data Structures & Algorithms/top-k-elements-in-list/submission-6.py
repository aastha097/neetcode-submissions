class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=Counter(nums) #{1:1,2:2,3:3}
        sorted_freq=dict(sorted(freq.items(),key=lambda item:item[1],reverse=True))
        #return k most freq ele
        l=[]
        for i,c in sorted_freq.items():
            l.append(i)
        return l[:k]
            
        
            
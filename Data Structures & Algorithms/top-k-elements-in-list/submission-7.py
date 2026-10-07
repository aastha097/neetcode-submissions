class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=Counter(nums)
        sorted_freq=dict(sorted(freq.items(),key=lambda items:items[1],reverse=True))
        l=[]
        for num,c in sorted_freq.items():
            if k!=0:
                l.append(num)
                k-=1
        return l
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap={}
        for i in nums:
            hashmap[i]=hashmap.get(i,0)+1
    
        result_values=sorted(hashmap.keys(),key=hashmap.get,reverse=True)
        for j in range(k):
            return result_values[:k]
            
            
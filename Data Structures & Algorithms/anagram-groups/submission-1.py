class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        amap=defaultdict(list)
        for s in strs:
            sorted_key=" ".join(sorted(s))
            amap[sorted_key].append(s)
        return list(amap.values())



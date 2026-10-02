class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        amap=defaultdict(list)
        for s in strs:
            sorted_str="".join(sorted(s))
            amap[sorted_str].append(s)
        return list(amap.values())



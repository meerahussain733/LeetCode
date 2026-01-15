class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for str in strs:
            sort_str=''.join(sorted(str))
            res[sort_str].append(str)
        return list(res.values())

        
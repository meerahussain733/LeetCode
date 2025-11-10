class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix=strs[0]
        for i, j in enumerate(prefix):
            for string in strs:
                if len(string) == i or string[i] != j:
                    return prefix[:i]
        return prefix
        

        
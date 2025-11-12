class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        if len(strs)==0:
            return ""
        k=""
        first=strs[0]
        last=strs[-1]
        for i in range(len(first)):
            if first[i]!=last[i]:
                break
            k+=first[i]
        return k
        

        
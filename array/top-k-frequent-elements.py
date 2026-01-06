class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_ele={}
        for element in nums:
            if element in freq_ele:
                freq_ele[element]+=1
            else:
                freq_ele[element]=1
        sorted_frq=sorted(freq_ele)
        return sorted_frq[:k]
        
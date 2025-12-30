class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_ele={}
        top_k=[]
        for element in nums:
            if element in freq_ele:
                freq_ele[element]+=1
            else:
                freq_ele[element]=1
        sorted_frq=sorted(freq_ele)
        for i in range(k):
            top_k.append(sorted_frq[i])
        return top_k

        
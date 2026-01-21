class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer=[]
        for i in range(len(nums)):
            product=1
            for j in range(len(nums)):
                if i!=j:
                    product=product*nums[j]
            answer.append(int(product))
        return answer

        
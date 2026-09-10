class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * (len(nums))

        totalProd = 1
        for i in nums:
            if i != 0: 
                totalProd *= i
        
        for i in range(0, len(nums)): 
            if nums[i] != 0: 
                output[i] = totalProd // nums[i]
            else: 
                output[i] = 0


        return output
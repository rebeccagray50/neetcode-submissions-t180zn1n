class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * (len(nums))

        totalProd = 1
        for i in nums:
            totalProd *= i
        
        for i in range(0, len(nums)-1): 
            output[i] = totalProd // nums[i]


        return output
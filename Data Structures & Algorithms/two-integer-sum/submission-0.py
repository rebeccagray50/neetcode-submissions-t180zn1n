class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)): 
            diff = target - nums[i]
            if diff in nums: 
                return [i, nums.index(diff)]
            else: 
                next
            
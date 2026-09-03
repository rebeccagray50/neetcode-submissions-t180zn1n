class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums)

        while left < right: 
            mid = left + ((right - left )// 2)

            if nums[mid] > target: 
                mid = right
            elif nums[mid] <= target: 
                mid = left+1
            
        return left-1 if (left and nums[left] == target) else -1
            
            
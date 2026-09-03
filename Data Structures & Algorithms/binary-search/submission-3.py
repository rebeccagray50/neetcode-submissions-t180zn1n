class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums)

        while left < right: 
            mid = left + ((right - left) // 2)
            if target < nums[mid]:
                right = mid
            elif target >= nums[mid]: 
                left = mid+1 

        return left -1 if (left and nums[left-1] == target) else -1 


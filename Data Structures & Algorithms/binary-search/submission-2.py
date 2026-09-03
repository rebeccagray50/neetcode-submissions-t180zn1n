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

        if (left and nums[left] == target): 
            return left
        else: 
            return -1


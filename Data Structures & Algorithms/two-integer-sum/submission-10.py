class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i in range(0, len(nums)-1): 
            map[nums[i]] = i 
        
        for i in nums: 
            difference = target - i 
            if difference in map: 
                return [map.get(i, 0), map.get(difference, 0)]
            

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}

        for i in range(0, len(nums)): 
            numMap[nums[i]] = i
        
        for index, num in enumerate(numMap):
            difference = target - num
            if difference in numMap: 
                return [index, numMap.get(difference, 0)]
            
        return [0, 0]
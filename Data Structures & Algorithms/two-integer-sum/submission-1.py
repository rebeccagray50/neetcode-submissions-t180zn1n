class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsMap = {} #value -> index
        for index, num in enumerate(nums):
            numsMap[num] = index

        for index, num in enumerate(nums): 
            difference = target - nums[index]
            if difference in numsMap and numsMap[difference] != index: 
                return [index, numsMap[difference]]
            
        return []


            
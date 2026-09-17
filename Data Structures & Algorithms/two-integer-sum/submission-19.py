class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for index in range(0, len(nums)):
            map[nums[index]] = index
        

        for i, v in enumerate(map):
            diff = target - v

            if diff in map and map.get(diff) != i: 
                return [i, map.get(diff, 0)]
            
        return [0,0]
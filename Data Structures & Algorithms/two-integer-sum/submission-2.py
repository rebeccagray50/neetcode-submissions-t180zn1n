class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {} #maps index to value

        #iterate through once to fill into map 
        for i, val in enumerate(nums):
            indices[val] = i
        
        #iterate to check 
        for i, val in enumerate(nums):
            diff = target - val
            if diff in indices and i != indices[diff]:
                return [i, indices[diff]]
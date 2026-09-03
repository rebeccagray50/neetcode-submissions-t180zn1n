class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}

        #add all to hm 
        for i in range(0, len(nums)): 
            indices[nums[i]] = i #num -> index

        #iterate through hm, get diff, check if contains 
        for index, num in enumerate(indices):
            diff = target - num
            if diff in indices: 
                return [index, indices[diff]]
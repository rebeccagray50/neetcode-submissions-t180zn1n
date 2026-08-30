class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices  = {} #val -> index

        #go through once and add to hm 
        for i in range(0, len(nums)): 
            indices[nums[i]] = i

        #go through again checking for diff in hm 
        for index, val in enumerate(indices): 
            diff = target - val
            if indices[diff] != index and diff in indices:
                return [index, indices[diff]]
        return [0 , 0]

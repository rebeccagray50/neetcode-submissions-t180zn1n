class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        marker = False
        position = 0
        for i in range(position+1, len(nums)):
            if nums[position] == nums[i]:
                return True
            else:
                position += 1
                self.hasDuplicate(nums[position:])

        return False
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numTracker = set()
        for i in nums: 
            if i in numTracker: 
                return True
            else: 
                numTracker.add(i)
        return False
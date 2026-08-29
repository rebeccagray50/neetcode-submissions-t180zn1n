class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numTrack = set()
        for i in nums:
            if i in numTrack:
                return True
            else: 
                numTrack.add(i)
            
        return False

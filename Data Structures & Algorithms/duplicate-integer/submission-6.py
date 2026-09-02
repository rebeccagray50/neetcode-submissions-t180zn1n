class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #create set 

        #add each item to set 
        #if x in set, return true

        numSet = set()

        for n in nums: 
            if n in numSet: 
                return True
            else: 
                numSet.add(n)
        
        return False
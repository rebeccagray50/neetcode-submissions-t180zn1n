class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ###index starts at 1 !!!!
        #return i1, i2 where i1+i2 == target
        #this looks like a hashmap problem like twosum1, but O(1) space needs tp
        l = 0 
        r = len(numbers)-1

        indices = [0, 0]
        bestSum = 0
        while l < r: 
            currentSum = numbers[l] + numbers[r]
            #as list is sorted, we know which direction to move 
            #based on whether sum is currently <> than target 
            if currentSum > target: 
                r -= 1
            elif currentSum < target: 
                l += 1
            else: 
                return [l+1, r+1]
        
        return []
    
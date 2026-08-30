class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        frequency = [[] for i in range(len(nums) + 1)]

        for n in nums: 
            count[n] = 1 + count.get(n, 0)
            
        for num, val in count.items(): 
            frequency[val].append(num)
        
        temp = []
        for i in range(len(frequency) - 1, 0, -1):
            for num in frequency[i]:
                temp.append(num)
                if len(temp) == k: 
                    return temp




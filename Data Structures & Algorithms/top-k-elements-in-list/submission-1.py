class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #set up a frequency list and counts h.mp
        count = {}

        freq = [[] for i in range(len(nums) + 1)]

        #iterate through numlist
        for n in nums: 
            #update count hashmap - at index (num), increment
            #frequency count by 1.
            count[n] = 1 + count.get(n, 0)

        #iterate through hashmap 
        for num, val in count.items():
            #add number to list at value position
            freq[val].append(num)
            
        #get k most freq elems  
        temp = []
        #iterate through from end to start
        for i in range((len(freq) - 1), 0, -1):
            #for items in frequency array
            for num in freq[i]:
                #add to output list
                temp.append(num)
                #until correct size 
                if len(temp) == k: 
                    return temp

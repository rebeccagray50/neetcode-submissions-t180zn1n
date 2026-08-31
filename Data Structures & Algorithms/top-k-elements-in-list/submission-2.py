class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        #len+1 as exclusive
        #the max frequency is size of list 
        freq = [[] for i in range(len(nums)+1)]
        
        #for each num in list, fill into hashmap
        for i in nums: 
            #increment freq count 
            count[i] = 1 + count.get(i, 0)

        for num, cnt in count.items():
            #add num to the 2d array at correct freq.
            #creates sorted list 
            freq[cnt].append(num)

        temp = []
        #runs from end of array to start
        for i in range(len(freq)-1, 0, -1): 
            #for each int in frequency count: 
            for num in freq[i]: 
                temp.append(num)
                #when temp correct length, return and end loop 
                if len(temp) == k: 
                    return temp 




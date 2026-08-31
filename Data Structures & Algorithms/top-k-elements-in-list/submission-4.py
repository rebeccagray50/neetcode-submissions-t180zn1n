class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} #
        ##needs to be +1
        freq = [[] for i in range(len(nums)+1)]

        #through hashmap 
        for n in nums: 
            count[n] = 1 + count.get(n, 0)
        

        #through freq list 
        for num, val in count.items(): 
            freq[val].append(num)
        
        #create return list 
        temp = []
        #through outer layer 
        for i in range(len(freq)-1, 0, -1): 
            #through inner 
            for inner in freq[i]: 
                temp.append(inner)
                if len(temp) == k: 
                    return temp 
        return []





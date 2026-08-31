class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # num -> count
        freq = [[] for i in range(len(nums)+1)]

        #iterate through and add to hm 
        for n in nums: 
            count[n] = 1 + count.get(n, 0)
        
        #iterate through hm for freqs
        for num, val in count.items(): 
            freq[val].append(num)

        #create list to return 
        temp = []
        #for each in freq
        #from end to beginning!!!
        #must be -1 for index
        for counts in range(len(freq)-1, 0, -1): 
            #for each in sublist 
            for n in freq[counts]: 
                temp.append(n) 
                
                if k == len(temp): 
                    return temp 

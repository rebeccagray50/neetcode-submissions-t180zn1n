class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)]

        #through hm 
        for i in nums: 
            count[i] = 1 + count.get(i, 0)

        #through freqs
        for num, val in count.items():
            freq[val].append(num)
            #add num to list at freq level 
        
        #create list to return 
        temp = []
        for outer in range(len(freq)-1, 0, -1):
            for inner in freq[outer]:
                temp.append(inner)
                if len(temp) == k: 
                    return temp 
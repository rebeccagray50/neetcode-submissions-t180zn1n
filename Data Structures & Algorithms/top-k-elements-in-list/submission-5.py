class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} #num -> val

        freq = [[] for i in range(len(nums)+1)]

        #iterate through hm 
        for n in nums: 
            count[n] = 1 + count.get(n, 0)

        #iterate through freqs 
        for num, val in count.items():
            freq[val].append(num)
        

        #create k list to return 
        temp = []
        #outer 
        for outer in range(len(freq)-1, 0, -1):
            for inner in freq[outer]:
                temp.append(inner)
                if len(temp) == k: 
                    return temp 




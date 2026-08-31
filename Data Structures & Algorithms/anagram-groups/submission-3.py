class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #create freq arrays and use these as keys in DICTIONARY 
        #conv to tuples 
        #then output DICTIONARY items
        count = defaultdict(list)

        #for each string
        for string in strs: 
            freq = [0] * 26
            #go through and create freq string 
            for c in string: 
                #increment count at char pos
                freq[ord(c) - ord('a')] += 1

            count[tuple(freq)].append(string)
        
        return list(count.values())
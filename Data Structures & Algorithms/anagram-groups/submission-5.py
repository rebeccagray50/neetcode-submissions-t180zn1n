class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for string in strs: 
            #init frequency array 
            freqCount = [0] * 26
            #for each character in each word
            for char in string: 
                freqCount[ord(char) - ord('a')] += 1
            anagrams[tuple(freqCount)].append(string)
        
        return list(anagrams.values())

    
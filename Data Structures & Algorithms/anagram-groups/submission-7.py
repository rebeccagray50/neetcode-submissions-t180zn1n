class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strList = defaultdict(list)

        for string in strs:
            freqList = [0] * 26

            for c in string: 
                temp = ord('a') - ord(c.lower())
                freqList[temp] += 1

            strList[tuple(freqList)].append(string)
        
        return strList.values()

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strList = defaultdict(list)
        for string in strs: 
            charCount = [0] * 26
            for c in string: 
                charCount[ord(c) - ord("a")] += 1
            
            strList[tuple(charCount)].append(string)
            
        return list(strList.values())

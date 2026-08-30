class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        stringList = defaultdict(list)
        for string in strs: 
            characterCount = [0] * 26
            for char in string: 
                characterCount[ord(char) - ord('a')] += 1
            
            #must convert to tuple (static) para use as key 
            #adding to list so use append
            stringList[tuple(characterCount)].append(string)
        
        return list(stringList.values())
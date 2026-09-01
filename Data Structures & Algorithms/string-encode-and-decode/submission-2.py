class Solution:

    def encode(self, strs: List[str]) -> str:
        mem = []
        for string in strs: 
            #add length of string e.g. 4
            mem.append(str(len(string)))
            #add delimiter
            mem.append("-")
            #then string
            mem.append(string)
        return "".join(mem) #combines all elements end to end

    def decode(self, s: str) -> List[str]:
        mem = []
        i = 0 

        #until end of string is reached
        while i < len(s): 
            j = i 
            #jump to next delimiter
            while s[j] != '-':
                j += 1 
            
            length = int(s[i:j])
            i = j+1
            j = i+length
            #add string alone to decoded list 
            mem.append(s[i:j])
            #start from next delim
            i = j
        
        return mem 
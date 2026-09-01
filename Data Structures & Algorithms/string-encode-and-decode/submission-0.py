class Solution:

    def encode(self, strs: List[str]) -> str:
        mem = []
        for string in strs: 
            mem.append(str(len(string)))
            mem.append("-")
            mem.append(string)
        return "".join(mem)

    def decode(self, s: str) -> List[str]:
        mem = []
        i = 0 

        while i < len(s): 
            j = i 
            while s[j] != '-':
                j += 1 
            length = int(s[i:j])
            i = j+1
            j = i+length
            mem.append(s[i:j])
            i = j
        
        return mem 
class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ''
        for i in strs:
            encoded_str+= str(len(i)) + '#' + i
        
        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_str  = []
        for i in range(len(s)):
            if s[i].isnumeric() and i+1 < len(s) and s[i+1] == '#':
                decoded_str.append(s[i+2 : i+2+int(s[i])])
        return decoded_str
        
            


class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for i in strs:
            encoded_str+= str(len(i)) + "$" + i
        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_str = []
        i = 0
        while i< len(s):
            if s[i].isdigit() and i+1 < len(s) and s[i+1]=="$":
                decoded_str.append(s[i+2: i+2+int(s[i])])
                i+= 2+int(s[i])
            else:
                i+=1
        return decoded_str
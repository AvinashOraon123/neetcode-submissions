class Solution:
    def isPalindrome(self, s: str) -> bool:
        without_alnum =''

        for i in range(len(s)-1, -1 , -1):
            if s[i].isalnum() and s[i]!= ' ':
                without_alnum+= s[i].lower()

        return without_alnum == without_alnum[::-1]

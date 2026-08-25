class Solution:
    def isPalindrome(self, s: str) -> bool:
        test_str = ''
        for i in range(len(s)):
            if s[i] != ' ' and s[i].isalnum() :
                test_str+= s[i].lower()

        return test_str[::-1] == test_str
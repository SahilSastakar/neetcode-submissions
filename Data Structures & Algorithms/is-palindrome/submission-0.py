class Solution:
    def isPalindrome(self, s: str) -> bool:
        print(s)
        
        s = "".join(c.lower() for c in s if c.isalnum())

        s1 = "".join(reversed(s))

        return s == s1
        
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        clean=[]
        for char in s:
            if char.isalnum():
                clean.append(char.lower())

        return clean==clean[::-1]
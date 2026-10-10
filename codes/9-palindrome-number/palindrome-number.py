class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """        
        xstr=str(x)
        if xstr==xstr[::-1]:
            return True
        else:
            return False
        
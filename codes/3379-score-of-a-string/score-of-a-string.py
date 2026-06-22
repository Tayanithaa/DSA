class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        score =0
        for n in range(len(s)-1):
            score += abs(ord(s[n])- ord(s[n+1]))

        return score
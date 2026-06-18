class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
       
        y=s.split()
        for i in range(len(y)):
            y[i]=y[i][::-1]
        return " ".join(y)


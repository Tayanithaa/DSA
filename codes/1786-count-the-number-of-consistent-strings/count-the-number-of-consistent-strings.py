class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        allowedset=set(allowed)
        count =0
        for  word in words:
            if all (char in allowedset for char in word):
                count+=1
        return count
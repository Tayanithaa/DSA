class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        for i in range(len(word)):
            if all(char.isupper() for char in word):
                return True
            elif word[0].isupper() and all(char.islower() for char in word[1:]):
                return True
            elif all(char.islower() for char in word):
                return True
            else:
                return False
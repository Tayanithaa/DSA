class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        return  command.replace ("G","G").replace("()","o").replace("(al)","al")

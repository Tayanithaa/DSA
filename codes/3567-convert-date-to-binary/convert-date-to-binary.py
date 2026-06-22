class Solution(object):
    def convertDateToBinary(self, date):
        """
        :type date: str
        :rtype: str
        """
        part = date.split('-')
        year=bin(int(part[0]))[2:]
        month=bin(int(part[1]))[2:]
        day=bin(int(part[2]))[2:]

        return year + "-" + month + "-" + day 
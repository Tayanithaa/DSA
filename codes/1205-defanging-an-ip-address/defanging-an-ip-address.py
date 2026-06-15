class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        ipv4=[]
        for i in range(len(address)):
            ipv4=address.replace(".", "[.]")
            return ipv4
class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        x1,y1,x2,y2= rec1[0],rec1[1],rec1[2],rec1[3]
        x3,y3,x4,y4 = rec2[0],rec2[1],rec2[2],rec2[3]

        if x2<=x3:
            return False
        if x1>=x4:
            return False
        if y2<=y3:
            return False
        if y1>=y4:
            return False

        return True
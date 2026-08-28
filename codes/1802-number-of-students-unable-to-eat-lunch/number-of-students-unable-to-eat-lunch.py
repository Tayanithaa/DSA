class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        c0=students.count(0)
        c1=students.count(1)
        for s in sandwiches:
            if s == 0 and c0>0:
                c0-=1
            elif s == 1 and c1>0:
                c1-=1
            else:
                break
        return c0+c1
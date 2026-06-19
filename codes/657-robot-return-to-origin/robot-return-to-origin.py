class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        # if (moves == "UD" or moves == "DU" or moves == "LR" or moves == "RL"):
        #     return True
        # else:
        #     return False

        return moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R')
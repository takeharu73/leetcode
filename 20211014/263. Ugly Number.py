class Solution:
    def isUgly(self, n: int) -> bool:
        """
        Solution
        1. Divide n by one of [1,2,3,5] and check if n can be divided or not
        2. If not, return false.
        """
        
        l_dividing = [2,3,5]
        if n <= 0:
            return False
        while True:
            flg = 0
            for d in l_dividing:
                if n%d == 0:
                    n = n/d
                    flg = 1
                    break
            if flg == 0:
                if n > 5:
                    return False
                else:
                    return True
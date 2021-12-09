class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = 0
        emptyBottles = 0
        while True:
            res += numBottles
            emptyBottles += numBottles 
            numBottles = emptyBottles // numExchange
            emptyBottles = emptyBottles % numExchange
            if numBottles == 0 and emptyBottles < numExchange:
                break
        return res
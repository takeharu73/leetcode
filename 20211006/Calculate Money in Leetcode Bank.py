class Solution:
    def totalMoney(self, n: int) -> int:
        """
        Process:
        1. Calculate n/7 and separate days to weeks O(1)
        2. Calculate the 1st day amount to put O(week_length)
        3. Calculate the total amount to put in each week O(week_length)
        4. Get the whole amount O(week_length)
        
        n = 10
        1 + 2 + 3 + 4 + 5 + 6 + 7 = (1+7)*7/2 = 28
        2 + 3 + 4
        -> 37
        
        O(week_length)
        """
        
        weeks = n//7
        remained_days = n%7
        
        total = 0
        # a = 1
        # for _ in range(weeks):
        #     sum_in_week = (a + (a+6)) * 7 / 2
        #     total += sum_in_week
        #     a += 1
        #     sum_in_week = sum_in_week + =7
        #     total += sum_in_week
        #     a += 1
            
        # for _ in range(remained_days):
        #     total += a
        #     a += 1

        total = 28 * weeks + 7 * ((weeks - 1) * weeks / 2)
            
        a = weeks + 1        
        total += (a + (a + remained_days - 1)) * remained_days / 2
    
        return int(total)
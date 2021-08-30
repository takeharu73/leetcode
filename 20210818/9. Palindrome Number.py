class Solution:
    def isPalindrome(self, x: int) -> bool:
        # with converting int to str
        
        
        
        
        
        # without converting to str, with calculating deivision of int
        # Ex)
        # 10**9 > 345676543 > 10**8
        # 345676543 >> 345676543//10**8 = 3 (same as last digit)
        # 345676543 - 10**8 * 3 = 45676543
        # (45676543 - 3) / 10 = 4567654
        # 4567654//10**6 = 4 (same as 2nd last digit)
        # 4567654 - 10**6 * 4 = 567654
        # (567654 - 4) / 10 = 56765
        # 56765//10**4 = 5 (same as 3rd last digit)
        # and so on..
        
        # Check the digits of x
        for i in range(11):
            if x/(10**i)<1:
                digit = i
                break
        
        # If x is less than 0, x is NOT palindrome integer.
        if x < 0:
            return False
        
        # If x is less than 0, x is NOT palindrome integer.
        if x == 0 or x == 1:
            return True
        
        # If x is 1 digit int, x is palindrome integer.
        elif digit == 1:
            return True
        
        # If x is 2 digits int, x will be palindrome integer if 1st digit number is the same as 2nd digit number.
        elif digit == 2:
            if x//10 == x%10:
                return True
            else:
                return False
        
        # Roop for digits and check quotient(1st digit) is the same as remainder(last digit)
        for i in range(digit, 0, -2):
            # If x digits is less than or equal to 2, judge if x is palindrome int or not by the same way
            if i == 1:
                return True
            elif i == 2:
                if x//10 == x%10:
                    return True
                else:
                    return False
                
            # If x digits is more than 2, check if the 1st digit is the same as the last digit
            else:
                # Quotient of x diveded by (10 ** digits)
                quot = x // (10**(i-1))
                # Remainder of x diveded by 10
                remain = x % 10
                if quot != remain:
                    return False
                else:
                    # If they are same, except 1st digit number and last digit number from x
                    x = x - quot * (10**(i-1))
                    x = (x - remain) / 10
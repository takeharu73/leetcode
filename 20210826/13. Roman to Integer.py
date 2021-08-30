class Solution:
    def romanToInt(self, s: str) -> int:
        """
        Condition:
        1 <= s.length <= 15
        s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
        It is guaranteed that s is a valid roman numeral in the range [1, 3999].
        """
        
        s_l = list(s)
        symbol_to_int = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        s_l = [symbol_to_int[s] for s in s_l]
        prev_i = s_l[0]
        result = 0
        for i in s_l:
            if i > prev_i:
                result += i
                result -= prev_i*2
            else:
                result += i
                prev_i = i
                
        return result
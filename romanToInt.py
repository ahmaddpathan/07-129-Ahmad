# visit https://leetcode.com/problems/roman-to-integer/description/ for problem description
class Solution:
    def romanToInt(self, s: str) -> int:
        rti = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        length = len(s)
        
        for i in range(length):
            cv = rti[s[i]]
            if i + 1 < length and cv < rti[s[i + 1]]:
                total -= cv
            else:  
                total += cv
        return total

 
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romanSymbols = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        stringLength = len(s)
        sum = 0
        stor = list(s)
        sum = sum + romanSymbols[s[0]]
        index_ = 1
        for element_ in s[1:]:
            if(romanSymbols[element_]):
                if((romanSymbols[element_] <= romanSymbols[s[index_ - 1]])):
                    sum += romanSymbols[element_]                    
                elif(romanSymbols[element_] > romanSymbols[s[index_ - 1]]):
                    sum = sum - romanSymbols[s[index_ - 1]]
                    calculateRoman = romanSymbols[element_] - romanSymbols[s[index_ - 1]]
                    sum += calculateRoman                                                           
                else:
                    pass
                index_ += 1
        return sum
    
  
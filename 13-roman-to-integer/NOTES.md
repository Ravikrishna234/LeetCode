def romanToInt(s):
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
    index_ = 0
    stor = list(s)
    for element_ in s:
        if(romanSymbols[element_]):
            if(index_ == 0):
                sum += romanSymbols[element_]
                index_ += 1
            elif(romanSymbols[element_] <= romanSymbols[s[index_ - 1]]):
                print(romanSymbols[s[index_ - 1]])
                print(str(sum) + "to check here")            	
                sum += romanSymbols[element_]
                index_ += 1
            else:
                calculateRoman = 0
                print(str(sum) + "here 1")
                sum = sum - romanSymbols[s[index_ - 1]]
                calculateRoman = romanSymbols[element_] - romanSymbols[s[index_ - 1]]               
                sum += calculateRoman
                print(str(sum) + "here 2")
                index_ += 1
                                                           
    return sum

if __name__ == '__main__':
    print(romanToInt('MCMXCIV'))  
    
  

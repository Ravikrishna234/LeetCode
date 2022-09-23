
import math
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index_i = 0
        index_j = 0
        
        while(index_i < len(s) and index_j < len(t)):
            if(s[index_i] == t[index_j]):
                index_i += 1
            index_j += 1
        # return len(s) == s
        return len(s) == index_i
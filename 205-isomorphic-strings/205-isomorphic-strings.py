
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False        
        thisdict = {}
        isomorphic = False
        for (a, b) in zip(list(s), list(t)):
            if thisdict.get(a):
                if(thisdict.get(a) != b):
                    return False
                else:
                    isomorphic = True
            else:
                if b not in thisdict.values(): 
                    thisdict[a] = b
                    isomorphic = True
                else:
                    return False
        return isomorphic
        
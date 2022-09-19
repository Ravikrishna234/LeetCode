class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # if(s.length)
        if(len(s) != len(t)):
            return False
        if(len(s) == 1):
            return s == t
        def convertStringTodict(s:str, dic: dict):
            for ch_ in s:
                if dic.get(ch_):
                    dic[ch_] = dic[ch_] + 1
                else:
                    dic[ch_] = 1
            return dic        

        isomorphicSource = {}
        isomorphicCompare = {}
        #for i in range(len(s)):
        zipped = dict(zip(s, t))
        print(zipped)
        #print(dict(zip(s, t))
        #    isomorphicTemp 
        #for i in range(len(s)):
        thisdict = {}
        # isomorphiv
        isomorphic = False
        for (a, b) in zip(list(s), list(t)):
            # if thisdict.get(a) and thisdict.get(a) == b:
            if thisdict.get(a):
                if(thisdict.get(a) != b):
                    return False
                else:
                    isomorphic = True
                # elif(thisdict.get(b) != a):
                    # return False
                    # isomorphic = True
            # elif: thisdict.get(b):
            #elif(thisdict.get(b)):
            #    if(thisdict.get(b) != a):
            #        return False
            #    else:
            #        isomorphic = True
            # elif thisdict.get(b):
                # if(thisdict.get(b) != a):
                    # return False
                # else:
                    # return True
                    # isomorphic = True
            else:
                # if
                # if b not in thisdict.valuea
                if b not in thisdict.values(): 
                    thisdict[a] = b
                
                    # thisdict[b] = a
                    print(thisdict)
                    isomorphic = True
                else:
                    # returj
                    return False
                # return False
        # return True
        return isomorphic

        isomorphicSource = convertStringTodict(s, isomorphicSource)
        isomorphicCompare = convertStringTodict(t, isomorphicCompare)
        # if(len(isomorphicSource) == len(isomorphicCompare)):
        #     for value in isomorphicCompare.values():
        #         if value not in isomorphicSource.values():
        #             return False
        #     return True
        
#    
#        print(zip(isomorphicSource.values(), isomorphicCompare.values()))





def findcommon(commonstr, onestr):
    commonstr_next = []
    for i in range(len(onestr),0,-1):
        for j in range(len(onestr)-i+1):
            if commonstr != "":
                # for commonstrone in commonstr:
                if onestr[j:j+i] in commonstr:
                    commonstr_next.append(onestr[j:j+i])
            else:
                commonstr_next.append(onestr[j:j+i])
                        
    return commonstr_next

def findcommon_prefix(commonstr, onestr):
    commonstr_next = []
    for i in range(len(onestr),0,-1):
        if commonstr != "":
            if onestr[:i] in commonstr:
                commonstr_next.append(onestr[:i])
        else:
            commonstr_next.append(onestr[:i])
                        
    return commonstr_next

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Write a function to find the longest common prefix string amongst an array of strings.
        If there is no common prefix, return an empty string.
        """
        
        commonstr = ""
        for i, onestr in enumerate(strs):
            commonstr = findcommon_prefix(commonstr, onestr)
            # print(commonstr)
        
        max_len = 0
        result = ""
        for onestr in commonstr:
            if max_len < len(onestr):
                result = onestr
                max_len = len(onestr)
        return result

"""
What I learned: 
1. I have to read question more precisely (Firstly I misunderstood question and I thought I have to check not only prefix but all contained strings. So I Wrote "findcommon" method).
2. To find common longest element, loop one by longer element to shorter element.

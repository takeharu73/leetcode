class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count_dict_r = {}
        count_dict_m = {}
        for s in list(ransomNote):
            if count_dict_r.get(s):
                count_dict_r[s] += 1
            else:
                count_dict_r[s] = 1
        for s in list(magazine):
            if count_dict_m.get(s):
                count_dict_m[s] += 1
            else:
                count_dict_m[s] = 1
        
        for s in count_dict_r.keys():
            if count_dict_m.get(s):
                if count_dict_r[s] > count_dict_m[s]:
                    return False
            else:
                return False
        return True
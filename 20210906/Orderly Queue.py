class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k > 1:
            return "".join(sorted(list(s)))
        else:
            list_s = list(s)
            s = min(list_s)
            min_string = "z"*len(list_s)
            for i in range(len(list_s)):
                list_s.append(list_s.pop(0))
                next_string = "".join(list_s)
                if next_string < min_string:
                    min_string = next_string
            return min_string
class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        pre_r = 0
        max_r = 0
        max_k = ""
        for r, k in list(zip(releaseTimes, list(keysPressed))):
            if max_r < r - pre_r:
                max_r = r - pre_r
                max_k = k
            elif max_r == r - pre_r:
                if k > max_k:
                    max_k = k
            pre_r = r
        return (max_k)
                
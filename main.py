class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        iter = 0
        ost = 0

        while n <= time :
            iter += 1
            time -= n - 1

        ost = time
        if iter % 2 == 0 :
            return ost + 1
        else :
            return n - ost

        return 0
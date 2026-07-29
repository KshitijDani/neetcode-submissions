from math import ceil

class Solution:
    def calcRate(self, piles: List[int], rate:int):
        hours = 0
        for pile in piles:
            hours+=ceil(pile/rate)

        return hours

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=1,max(piles)

        while l<=r:
            rate = l + (r-l)//2
            hours = self.calcRate(piles, rate)
            if hours <= h:
                #if the koko is eating too fast, then the overall rate needs to lower than the current value
                # also we need to find the lowest possible rate, so even if we find one that fits until the end of the overall loop
                r=rate-1
            else:
                l=rate+1

        return l
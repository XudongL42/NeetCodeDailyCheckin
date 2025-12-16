class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        pile_sum, pile_max = 0, 0
        for pile in piles:
            pile_sum += pile
            pile_max = max(pile_max, pile)
        k_min = (pile_sum + h -1)//h
        k_max = pile_max // (h//len(piles)) + 1

        while k_min < k_max:
            k_mid = (k_min + k_max)//2
            h_mid = self.calculateHours(piles, k_mid)
            print(f"h_mid: {h_mid}, k_mid:{k_mid}, {k_min}:{k_max}")
            if h_mid > h:
                # took too long, need higher speed
                k_min = k_mid + 1
            else:
                # Still have room to reduce the speed
                k_max = k_mid

        return k_min
            
    

    # return how many hours it take to finish eating given a speed k
    def calculateHours(self, piles: List[int], k: int) -> int:
        result = 0
        for pile in piles:
            result += (pile + k -1)//k
        return result
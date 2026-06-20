class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        result = high

        while low <= high:
            mid = (low + high) //2

            total_hours = 0
            for p in piles:
                total_hours += (p + mid - 1) // mid

            if total_hours <= h:
                result = mid
                high = mid - 1
            else:
                low = mid + 1

        return result 

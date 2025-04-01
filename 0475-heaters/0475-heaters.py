class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        
        def validate(rad, houses, heaters):            
            p = 0
            for i in range(len(houses)):
                while p < len(heaters) and (heaters[p] - rad > houses[i] or houses[i] > heaters[p] + rad):
                    p += 1

                if p >= len(heaters):
                    return False
            return True

        heaters.sort()
        houses.sort()
        l = 0
        r = max(max(heaters), max(houses)) - min(houses)

        while l <= r:
            mid = (l + r) // 2

            if validate(mid, houses, heaters):
                r = mid - 1
            else:
                l = mid + 1
            
        return l
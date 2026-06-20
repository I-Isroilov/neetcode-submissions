class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        fleets = 0
        last_time_fleet = 0

        for p, s in cars:
            ttr = (target - p) / s
            if ttr > last_time_fleet:
                fleets += 1
                last_time_fleet = ttr

        return fleets
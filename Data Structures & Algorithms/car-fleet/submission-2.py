class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse = True)
        fleets = 0
        last_fleet_time = 0

        for p, s in cars:
            ttr = (target - p) / s

            if ttr > last_fleet_time:
                fleets += 1
                last_fleet_time = ttr
        return fleets

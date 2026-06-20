class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)

        stack = []

        for p, s in cars:
            ttr = (target - p) / s

            if not stack or ttr > stack[-1]:
                stack.append(ttr)

        return len(stack)
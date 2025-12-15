# Don't need to use stack at all as all we need is a count
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # form a list for tuple for sorting
        cars = sorted([(position[i], speed[i]) for i in range(len(position))], key=lambda x:x[0], reverse=True)

        fleets = 1
        time_to_dest = (target - cars[0][0])/cars[0][1]
        for i in range(1, len(position)):
            cur_time_to_dest = (target - cars[i][0])/cars[i][1]
            if time_to_dest < cur_time_to_dest:
                #This car cannot catch up the previous fleet, form a new fleet
                fleets += 1
                time_to_dest = cur_time_to_dest
        return fleets


class Solution2:
    # Updated version with AI suggestion
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # form a list for tuple for sorting
        cars = sorted(zip(position, speed), reverse=True)
        fleets = 0
        time_to_dest = 0.0
        for pos, spd in cars:
            updated_time_to_dest = float("inf") if spd == 0 else (target - pos)/spd
            if updated_time_to_dest > time_to_dest:
                time_to_dest = updated_time_to_dest
                fleets += 1

        return fleets
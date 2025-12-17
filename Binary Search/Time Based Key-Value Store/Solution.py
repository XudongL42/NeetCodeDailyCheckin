from collections import defaultdict

class TimeMap:

    def __init__(self):
        # Map of key:list([timestamp,value])
        self.key_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_map[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        value_list = self.key_map[key]

        if not value_list:
            return ""

        left, right = 0, len(value_list) - 1

        result = ""
        while left <= right:
            mid = (left + right) // 2
            mid_time = value_list[mid][0]
            if mid_time > timestamp:
                right = mid - 1
            elif mid_time == timestamp:
                return value_list[mid][1]
            else:
                #mid value smaller than timestamp:
                result = value_list[mid][1]
                left = mid + 1
        
        return result
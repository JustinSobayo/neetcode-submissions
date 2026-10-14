class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)



        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((timestamp, value))


        
        

    def get(self, key: str, timestamp: int) -> str:
        #if not value at timestamp: retrun value at prev timestamp if not prev time stamp: ""
        # i want to retrun every value, timestamp tuple inside of a list and do binary search on the list in order to find the value of the key at the specific timestamp so do binary search where the search area is the timestamp
        right_tupleI = len(self.time_map[key]) - 1
        left_tupleI = 0
        res = ''
        while left_tupleI <= right_tupleI:
            mid_tupleI = (right_tupleI + left_tupleI) // 2
            if self.time_map[key][mid_tupleI][0] == timestamp:
                return self.time_map[key][mid_tupleI][1]
            elif self.time_map[key][mid_tupleI][0] > timestamp:
                right_tupleI = mid_tupleI - 1
            #if the mid timestamp is less than timestamp
            #we want to search right
            elif self.time_map[key][mid_tupleI][0] <= timestamp:
                left_tupleI = mid_tupleI + 1
                res = self.time_map[key][mid_tupleI][1]
        return res

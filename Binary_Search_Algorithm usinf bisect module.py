# Binary search algorithm searhing by keys

import bisect


class SearchBy:
    def __init__(self, key, elements):
        self.elements_by_key = sorted([(key(x), x) for x in elements])
        self.keys = [x[0] for x in self.elements_by_key]
        
    def find(self, value):
        index = bisect.bisect_left(self.keys, value)
        if index < len(self.keys) and self.keys[index] == value:
            return self.elements_by_key[index][1]


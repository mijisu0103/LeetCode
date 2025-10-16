class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
            
        intervals.sort()
        merged = [intervals[0]]
        
        for current in intervals[1:]:
            if merged[-1][1] >= current[0]:
                merged[-1][1] = max(merged[-1][1], current[1])
            else:
                merged.append(current)
        
        return merged
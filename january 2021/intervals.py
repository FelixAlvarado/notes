# merge intervals
# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

# Example 1:

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
# Example 2:

# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
# my answer
from operator import itemgetter

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#     go through array
# for each element, check to see if the start point is less than the previous result elements end point. if so, modify endpoint to be end point of current element. 
# if not, add current element to result

        result = []
    
        intervals = sorted(intervals,key=itemgetter(0))
        
        for interval in intervals:
            if len(result) == 0: 
                result.append(interval)
            elif interval[0] <= result[-1][1] and interval[1] > result[-1][1]:
                result[-1][1] = interval[1]
            elif interval[0] > result[-1][1]:
                result.append(interval)
        
        return result
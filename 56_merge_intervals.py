"""
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18]. 
"""
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param {Interval[]} intervals
    # @return {Interval[]}
    def merge(self, intervals):
        """
        1. sort the intervals by starting point.
        2. iterate through
        3. if curr.start <= prev.end, merge
        4. else append, prev = curr
        """
        results = []
        intervals.sort(key=lambda x: x.start)
        for interval in intervals:
            if len(results) > 0 and interval.start <= results[-1].end:
                results[-1].end = max(results[-1].end, interval.end)
            else:
                results.append(interval)

        return results

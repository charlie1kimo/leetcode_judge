"""
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:
Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10]. 
"""
# Definition for an interval.
#class Interval:
#    def __init__(self, s=0, e=0):
#        self.start = s
#        self.end = e
#
#    def __repr__(self):
#        return "<Interval: (%d, %d)>" % (self.start, self.end)

class Solution:
    # @param {Interval[]} intervals
    # @param {Interval} newInterval
    # @return {Interval[]}
    def insert(self, intervals, newInterval):
        """
        1. find start, end index
        2. if start == end, copy intervals, insert at start
        3. merge case:
            copy up to start
            new_interval = Interval(
                                s = min(start.start, newInterval.start),
                                e = max(end-1.end, newInterval.end)
                            )
            copy from end to len()
        """
        results = []
        start = 0
        end = 0

        if intervals == None or len(intervals) == 0:
            results.append(newInterval)
            return results

        for index, interval in enumerate(intervals):
            if newInterval.start > interval.end:        # non-overlap start
                start += 1
            if newInterval.end >= interval.start:       # overlap end
                end += 1
            else:
                break

        if start == end:
            results += intervals
            results.insert(start, newInterval)
            return results

        for i in range(start):
            results.append(intervals[i])

        new_interval = Interval(
            s = min(intervals[start].start, newInterval.start),
            e = max(intervals[end-1].end, newInterval.end)
        )
        results.append(new_interval)

        results += intervals[end:]

        return results


if __name__ == "__main__":
    sol = Solution()
    print sol.insert([], Interval(5, 7))
    print sol.insert([Interval(1, 5)], Interval(6, 8))

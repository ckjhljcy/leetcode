import heapq
# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class SummaryRanges(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.intervals = list()

    def addNum(self, val):
        """
        :type val: int
        :rtype: void
        """
        self.intervals.append(val)

    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        result = []
        self.intervals = list(set(self.intervals))
        self.intervals.sort()
        start = 0
        if len(self.intervals) == 1:
            return [Interval(self.intervals[0], self.intervals[0])]
        for index in range(0, len(self.intervals)-1):
            if self.intervals[index+1] == self.intervals[index] + 1:
                continue
            else:
                end = index
                result.append(Interval(self.intervals[start], self.intervals[end]))
                start = index + 1
        result.append(Interval(self.intervals[start], self.intervals[-1]))
        return result

class SummaryRanges2(object):

        def __init__(self):
            self.intervals = []

        def addNum(self, val):
            heapq.heappush(self.intervals, (val, Interval(val, val)))

        def getIntervals(self):
            stack = []
            while self.intervals:
                idx, cur = heapq.heappop(self.intervals)
                if not stack:
                    stack.append((idx, cur))
                else:
                    _, prev = stack[-1]
                    if prev.end + 1 >= cur.start:
                        prev.end = max(prev.end, cur.end)
                    else:
                        stack.append((idx, cur))
            self.intervals = stack
            return list(map(lambda x: x[1], stack))

# Your SummaryRanges object will be instantiated and called as such:
obj = SummaryRanges2()
obj.addNum(1)
param_2 = obj.getIntervals()
obj.addNum(3)
param_2 = obj.getIntervals()
obj.addNum(7)
param_2 = obj.getIntervals()
obj.addNum(2)
param_2 = obj.getIntervals()
obj.addNum(6)
param_2 = obj.getIntervals()
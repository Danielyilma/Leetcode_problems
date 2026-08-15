class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        print(intervals)
        start, end = intervals[0]
        res = []

        for i in range(1, len(intervals)):
            # if there is overlap between the two adjecent indexes
            if end >= intervals[i][0]:
                end = max(end, intervals[i][1])
            else:
                res.append([start, end])
                start, end = intervals[i]

        res.append([start, end])

        return res
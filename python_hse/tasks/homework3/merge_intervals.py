"""
Task info:
https://leetcode.com/problem-list/array/
url: https://leetcode.com/problems/merge-intervals/
"""


class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        if len(intervals) == 1:
            return intervals

        intervals.sort(key=lambda x: x[0])
        result: list[list[int]] = []
        interval = intervals[0]

        for intrvl in intervals[1:]:
            if intrvl[0] <= interval[1]:
                interval[1] = max(interval[1], intrvl[1])
            else:
                result.append(interval)
                interval = intrvl

        result.append(interval)
        return result

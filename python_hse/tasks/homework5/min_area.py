"""
Task info:
https://leetcode.com/problem-list/hash-table/
url: https://leetcode.com/problems/minimum-area-rectangle
"""


class Solution:
    def minAreaRect(self, points: list[list[int]]) -> int:
        lines: dict[int, list[int]] = dict()

        for x, y in points:
            if x not in lines:
                lines[x] = []
            lines[x].append(y)

        last_seen: dict[tuple[int, int], int] = {}
        min_area = -1

        for x in sorted(lines.keys()):
            y_list = sorted(lines[x])

            for i in range(len(y_list)):
                for j in range(i + 1, len(y_list)):
                    y1, y2 = y_list[i], y_list[j]

                    if (y1, y2) in last_seen:
                        prev_x = last_seen[(y1, y2)]
                        area = (x - prev_x) * (y2 - y1)
                        if min_area == -1:
                            min_area = area

                        min_area = min(min_area, area)

                    last_seen[(y1, y2)] = x

        return min_area if min_area != -1 else 0

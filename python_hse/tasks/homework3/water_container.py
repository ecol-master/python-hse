"""
Task info:
https://leetcode.com/problem-list/array/
url: https://leetcode.com/problems/container-with-most-water/description
"""


class Solution:
    def maxArea(self, height: list[int]) -> int:
        right = len(height) - 1
        left = 0

        mx_area: int = 0

        while right != left:
            new_area: int = (right - left) * min(height[left], height[right])
            mx_area = max(mx_area, new_area)

            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return mx_area

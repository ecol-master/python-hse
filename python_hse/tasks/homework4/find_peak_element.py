"""
Task info:
https://leetcode.com/problem-list/array/
url: https://leetcode.com/problems/find-peak-element/
"""


class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        left: int = 0
        right: int = len(nums) - 1

        while left != right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1

        return left

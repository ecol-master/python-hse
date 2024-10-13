"""
Task info:
https://leetcode.com/problem-list/array/
url: https://leetcode.com/problems/first-missing-positive/description/
"""


class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n: int = len(nums)

        i: int = 0
        while i != n:
            ind = nums[i] - 1
            if nums[i] >= 1 and nums[i] <= n and nums[i] != nums[ind]:
                nums[i], nums[ind] = nums[ind], nums[i]
            else:
                i += 1

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1

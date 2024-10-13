"""
Task info:
https://leetcode.com/problem-list/array/
url: https://leetcode.com/problems/sort-colors/description
"""


class Solution:
    def sortColors(self, nums: list[int]) -> None:
        b_ind: int = len(nums) - 1
        r_ind: int = 0

        ind: int = 0

        while ind <= b_ind:
            print(nums)
            if nums[ind] == 0:
                nums[r_ind], nums[ind] = nums[ind], nums[r_ind]
                r_ind += 1

            if nums[ind] == 2:
                nums[b_ind], nums[ind] = nums[ind], nums[b_ind]
                b_ind -= 1
                continue

            ind += 1

"""
Task info:
https://leetcode.com/problem-list/hash-table/
url: https://leetcode.com/problems/majority-element-ii/
"""


class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        count1, count2 = 0, 0
        cand1, cand2 = 0, 0

        for num in nums:
            if count1 == 0 and num != cand2:
                count1 = 1
                cand1 = num
            elif count2 == 0 and num != cand1:
                count2 = 1
                cand2 = num
            elif cand1 == num:
                count1 += 1
            elif cand2 == num:
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1

        k = len(nums) // 3

        count1, count2 = 0, 0
        for num in nums:
            if cand1 == num:
                count1 += 1
            elif cand2 == num:
                count2 += 1

        if count1 > k and count2 > k:
            return [cand1, cand2]

        if count1 > k:
            return [cand1]

        if count2 > k:
            return [cand2]

        return []

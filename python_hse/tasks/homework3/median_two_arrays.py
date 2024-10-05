"""
Task info:
https://leetcode.com/problem-list/array/
url: https://leetcode.com/problems/median-of-two-sorted-arrays
"""


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        if (len(nums1) + len(nums2)) == 1:
            return sum(nums1) + sum(nums2)

        if len(nums1) + len(nums2) == 2:
            return (sum(nums1) + sum(nums2)) / 2

        i, j = 0, 0

        med: int = (len(nums1) + len(nums2)) // 2

        prev_elem = 0
        last_elem = 0

        while (i + j) <= med:
            if i == len(nums1):
                prev_elem = last_elem
                last_elem = nums2[j]
                j += 1
                continue

            if j == len(nums2):
                prev_elem = last_elem
                last_elem = nums1[i]
                i += 1
                continue

            if nums1[i] < nums2[j]:
                prev_elem = last_elem
                last_elem = nums1[i]
                i += 1
            else:
                prev_elem = last_elem
                last_elem = nums2[j]
                j += 1

        return (
            last_elem
            if (len(nums1) + len(nums2)) % 2 == 1
            else (last_elem + prev_elem) / 2
        )

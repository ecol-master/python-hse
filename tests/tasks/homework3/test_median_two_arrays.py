from python_hse.tasks.homework3.median_two_arrays import Solution


def test_median_two_arrays():
    cases: list[tuple[list[int], list[int], float]] = [
        ([1, 3], [2], 2),
        ([1, 2], [3, 4], 2.5),
    ]
    solution = Solution()
    for case in cases:
        assert solution.findMedianSortedArrays(case[0], case[1]) == case[2]

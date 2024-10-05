from python_hse.tasks.homework3.merge_intervals import Solution


def test_merge_intervals():
    cases: list[tuple[list[list[int]], list[list[int]]]] = [
        ([[2, 3], [2, 2], [3, 3], [1, 3], [5, 7], [2, 2], [4, 6]], [[1, 3], [4, 7]])
    ]

    solution = Solution()
    for case in cases:
        assert solution.merge(case[0]) == case[1]

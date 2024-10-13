from python_hse.tasks.homework4.first_missing_positive import Solution


def test_first_missing_poisitive():
    cases: list[tuple[list[int], int]] = [
        ([1, 2, 0], 3),
        ([3, 4, -1, 1], 2),
        ([7, 8, 9, 11, 12], 1),
        ([0], 1),
        ([1, 1], 2),
    ]
    solution = Solution()
    for case in cases:
        assert solution.firstMissingPositive(case[0]) == case[1]

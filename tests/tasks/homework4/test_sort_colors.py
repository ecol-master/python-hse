from python_hse.tasks.homework4.sort_colors import Solution


def test_sort_colors():
    cases: list[tuple[list[int], list[int]]] = [
        ([2, 0, 1], [0, 1, 2]),
        ([2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2]),
        ([1, 2, 0], [0, 1, 2]),
    ]

    solution = Solution()
    for case in cases:
        solution.sortColors(case[0])
        assert case[0] == case[1]

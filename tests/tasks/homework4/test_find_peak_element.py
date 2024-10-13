from python_hse.tasks.homework4.find_peak_element import Solution


def test_find_peak_element():
    cases: list[tuple[list[int], list[int]]] = [
        ([1, 2, 3, 1], [2]),
        ([1, 2, 1, 3, 5, 6, 4], [1, 5]),
    ]

    solution = Solution()
    for case in cases:
        assert solution.findPeakElement(case[0]) in case[1]

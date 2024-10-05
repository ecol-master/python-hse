from python_hse.tasks.homework3.water_container import Solution


def test_water_container():
    cases: list[tuple[list[int], int]] = [
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ([1, 1], 1),
    ]
    solution = Solution()
    for case in cases:
        assert solution.maxArea(case[0]) == case[1]

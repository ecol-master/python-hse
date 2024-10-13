from python_hse.tasks.homework4.plus_one import Solution


def test_plus_one():
    cases: list[tuple[list[int], list[int]]] = [([1, 2, 3], [1, 2, 4]), ([9], [1, 0])]

    solution = Solution()
    for case in cases:
        assert solution.plusOne(case[0]) == case[1]

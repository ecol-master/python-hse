from typing import List
from typing import Tuple

from python_hse.tasks.homework2.combinations_phone_number import Solution


def test_combs_phone_number():
    cases: List[Tuple[str, List[str]]] = [
        ("23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
    ]

    solution = Solution()

    for case in cases:
        result = solution.letterCombinations(case[0])
        assert len(result) == len(case[1])

        for v in result:
            assert v in case[1]

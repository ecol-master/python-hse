from typing import List
from typing import Tuple

from python_hse.tasks.homework2.word_break import Solution


def test_word_break():
    cases: List[Tuple[str, List[str], bool]] = [
        ("aaaaaaaa", ["aaaa", "aaa", "aa"], True),
        ("abcd", ["a", "abc", "b", "cd"], True),
        (
            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
            [
                "a",
                "aa",
                "aaa",
                "aaaa",
                "aaaaa",
                "aaaaaa",
                "aaaaaaa",
                "aaaaaaaa",
                "aaaaaaaaa",
                "aaaaaaaaaa",
            ],
            False,
        ),
    ]

    solution = Solution()
    for case in cases:
        assert solution.wordBreak(case[0], case[1]) == case[2]

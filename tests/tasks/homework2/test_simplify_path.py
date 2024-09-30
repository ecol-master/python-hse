# import pytest
from typing import List
from typing import Tuple

from python_hse.tasks.homework2.simplify_path import Solution


def test_simplify_path():
    solution = Solution()
    cases: List[Tuple[str, str]] = [
        ("/home/", "/home"),
        ("/home//foo/", "/home/foo"),
        ("/home/user/Documents/../Pictures", "/home/user/Pictures"),
        ("/../", "/"),
        ("/.../a/../b/c/../d/./", "/.../b/d"),
    ]

    for case in cases:
        assert solution.simplifyPath(case[0]) == case[1]

from typing import List

"""
Task info:
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/simplify-path/description/
"""


class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs: List[str] = []

        for dir in path.split("/"):
            dir = dir.strip()

            if not dir:
                continue

            if dir == ".." and len(dirs):
                dirs.pop()
                continue
            elif dir == "." or dir == "..":
                continue

            dirs.append(dir)

        if not len(dirs):
            return "/"
        else:
            return "/" + "/".join(dirs)

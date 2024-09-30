"""
Task info:
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/design-add-and-search-words-data-structure/description/
"""


class WordDictionary:
    def __init__(self):
        self.words: dict[str, list[str]] = {}

    def addWord(self, word: str) -> None:
        if word[0] in self.words.keys():
            self.words[word[0]].append(word)
        else:
            self.words[word[0]] = [word]

    def search(self, word: str) -> bool:
        if word[0] not in self.words.keys() and word[0] != ".":
            return False

        ks = [word[0]] if word[0] != "." else self.words.keys()
        for k in ks:
            for w in self.words[k]:
                if len(word) != len(w):
                    continue

                if all(w[i] == word[i] or word[i] == "." for i in range(len(word))):
                    return True

        return False

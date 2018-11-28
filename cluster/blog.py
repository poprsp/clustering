#!/usr/bin/env python3

from typing import List


class Word:
    def __init__(self, word: str, count: float) -> None:
        self._word = word
        self._count = count

    @property
    def word(self) -> str:
        return self._word

    @property
    def count(self) -> float:
        return self._count


class Blog:
    def __init__(self, name: str) -> None:
        self._name = name
        self._words = []  # type: List[Word]

    def add_word(self, word: Word) -> None:
        self._words.append(word)

    def find_word(self, w: str) -> Word:
        for word in self._words:
            if word.word == w:
                return word
        raise RuntimeError("Missing word {}".format(w))

    @property
    def words(self) -> List[Word]:
        return self._words

    @property
    def name(self) -> str:
        return self._name


def parse_blogs(path: str) -> List[Blog]:
    """
    Parse the data and build a variable number of clusters.

    Args:
        path: Path to the dataset

    Returns:
        list: A list of clusters
    """
    blogs = {}  # type: dict

    with open(path, "r") as f:
        # The first line is: Blog word1 word2 ...
        _, *words = [field.strip() for field in f.readline().split("\t")]

        for line in f.readlines():
            # All other lines are: blog-name count1 count2 ...
            name, *counts = [field.strip() for field in line.split("\t")]
            if name not in blogs.keys():
                blogs[name] = Blog(name)
            blog = blogs[name]

            for i in range(len(words)):
                blog.add_word(Word(words[i], float(counts[i])))

    return list(blogs.values())
